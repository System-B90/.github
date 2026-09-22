"""
Name: test_wait_for_hive.py
Purpose: Branch coverage for actions/setup-hive/wait-for-hive.sh, driven
         through stubbed curl/sleep binaries on PATH. Nothing is fetched and
         the suite does not wait out the script's real 5s-per-attempt budget.
Created: 2026-09-20
Author: Michael K. Steinberg
"""

import os
import shutil
import subprocess
import sys
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parents[1] / "actions" / "setup-hive" / "wait-for-hive.sh"

pytestmark = pytest.mark.skipif(
    sys.platform == "win32", reason="bash script; the runner leg that matters is Linux"
)


@dataclass
class Result:
    returncode: int
    stdout: str
    calls: list[str]

    def called(self, needle: str) -> bool:
        return any(needle in call for call in self.calls)

    def logged(self, needle: str) -> bool:
        return needle in self.stdout

    @property
    def attempts(self) -> int:
        return sum(1 for call in self.calls if call.startswith("curl"))


@pytest.fixture
def harness(tmp_path: Path) -> Iterator[Path]:
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (tmp_path / "calls.log").write_text("")
    record = f'echo "$(basename "$0") $*" >> "{tmp_path}/calls.log"'
    (bin_dir / "sleep").write_text(f"#!/usr/bin/env bash\n{record}\nexit 0\n")
    (bin_dir / "sleep").chmod(0o755)
    yield tmp_path


def _run(
    harness: Path,
    *,
    codes: list[str],
    attempts: int = 5,
    curl_exit: int = 0,
) -> Result:
    """Runs the wait with curl reporting `codes` in order (last one repeats)."""
    code_file = harness / "codes"
    code_file.write_text("\n".join(codes))
    counter = harness / "curl.count"
    counter.write_text("0")

    stub = harness / "bin" / "curl"
    stub.write_text(
        f"""#!/usr/bin/env bash
echo "curl $*" >> "{harness}/calls.log"
n=$(cat "{counter}")
echo $((n + 1)) > "{counter}"
mapfile -t c < "{code_file}"
idx=$n
[ "$idx" -ge "${{#c[@]}}" ] && idx=$(( ${{#c[@]}} - 1 ))
printf '%s' "${{c[$idx]}}"
exit {curl_exit}
"""
    )
    stub.chmod(0o755)

    env = dict(os.environ)
    env["PATH"] = f"{harness / 'bin'}{os.pathsep}{env['PATH']}"
    env["HIVE_HOSTNAME"] = "hive.test"
    env["WAIT_ATTEMPTS"] = str(attempts)
    proc = subprocess.run(
        ["bash", str(_SCRIPT)], capture_output=True, text=True, env=env, check=False
    )
    return Result(
        returncode=proc.returncode,
        stdout=proc.stdout,
        calls=(harness / "calls.log").read_text().splitlines(),
    )


def test_a_200_ends_the_wait_immediately(harness: Path) -> None:
    result = _run(harness, codes=["200"])

    assert result.returncode == 0
    assert result.logged("Hive is up (HTTP 200)")
    assert result.attempts == 1


def test_a_redirect_counts_as_up(harness: Path) -> None:
    # An unauthenticated GET of / is expected to redirect; treating 3xx as
    # not-ready would time out against a perfectly healthy stack.
    result = _run(harness, codes=["302"])

    assert result.returncode == 0
    assert result.logged("Hive is up (HTTP 302)")


def test_a_401_counts_as_up(harness: Path) -> None:
    # Likewise 4xx: the stack is serving, it just will not serve *us*.
    result = _run(harness, codes=["401"])

    assert result.returncode == 0
    assert result.logged("Hive is up (HTTP 401)")


def test_a_502_keeps_waiting(harness: Path) -> None:
    # 5xx is nginx up but core not yet -- the one case where more waiting is
    # exactly right.
    result = _run(harness, codes=["502", "502", "200"], attempts=5)

    assert result.returncode == 0
    assert result.attempts == 3
    assert result.logged("HTTP 502")


def test_a_dead_socket_keeps_waiting(harness: Path) -> None:
    result = _run(harness, codes=["000", "200"], attempts=5, curl_exit=7)

    assert result.returncode == 0
    assert result.attempts == 2


def test_the_wait_is_bounded_and_exits_nonzero_on_timeout(harness: Path) -> None:
    result = _run(harness, codes=["502"], attempts=3)

    assert result.returncode == 1
    assert result.logged("::error::Hive failed to become ready in time")
    # Bounded: exactly the configured attempts, never a loop that hangs the box.
    assert result.attempts == 3


def test_tls_verification_is_skipped_for_the_stack_self_signed_cert(harness: Path) -> None:
    result = _run(harness, codes=["200"])

    assert result.called("-ks")
    assert result.called("https://hive.test/")


def test_a_curl_that_prints_nothing_does_not_wedge_the_loop(harness: Path) -> None:
    # An empty code would make every comparison a bash error rather than a
    # not-ready verdict; the default keeps the loop bounded and honest.
    result = _run(harness, codes=[""], attempts=2, curl_exit=1)

    assert result.returncode == 1
    assert result.attempts == 2
    assert result.logged("HTTP 000")


def test_script_passes_shellcheck() -> None:
    if not shutil.which("shellcheck"):
        pytest.skip("shellcheck not installed")

    proc = subprocess.run(["shellcheck", str(_SCRIPT)], capture_output=True, text=True, check=False)
    assert proc.returncode == 0, proc.stdout
