"""
Name: test_wait_for_postgres.py
Purpose: Branch coverage for actions/setup-hive/wait-for-postgres.sh, driven
         through stubbed docker/sleep binaries on PATH. The loop's real budget
         is minutes; the sleep stub returns immediately so the suite does not.
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

_SCRIPT = Path(__file__).resolve().parents[1] / "actions" / "setup-hive" / "wait-for-postgres.sh"

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
    def sleeps(self) -> int:
        return sum(1 for call in self.calls if call.startswith("sleep"))

    @property
    def tcp_probes(self) -> int:
        return sum(1 for call in self.calls if "pg_isready" in call)


@pytest.fixture
def harness(tmp_path: Path) -> Iterator[Path]:
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (tmp_path / "calls.log").write_text("")
    record = f'echo "$(basename "$0") $*" >> "{tmp_path}/calls.log"'
    # The script sleeps 5s per attempt. Nothing here depends on wall time.
    (bin_dir / "sleep").write_text(f"#!/usr/bin/env bash\n{record}\nexit 0\n")
    (bin_dir / "sleep").chmod(0o755)
    yield tmp_path


def _run(
    harness: Path,
    *,
    statuses: list[str],
    attempts: int = 5,
    has_healthcheck: bool = True,
    tcp_ok: bool = True,
) -> Result:
    """Runs the wait with `docker inspect` yielding `statuses` in order.

    The last status repeats once the list is exhausted, so a test only has to
    spell out the interesting prefix.
    """
    status_file = harness / "statuses"
    status_file.write_text("\n".join(statuses))
    counter = harness / "inspect.count"
    counter.write_text("0")

    stub = harness / "bin" / "docker"
    stub.write_text(
        f"""#!/usr/bin/env bash
echo "docker $*" >> "{harness}/calls.log"
case "$2" in
  --format)
    case "$3" in
      *State.Health\\}}\\}}yes*)
        {"echo yes" if has_healthcheck else "echo"}
        exit 0 ;;
      *Health.Status*)
        n=$(cat "{counter}")
        echo $((n + 1)) > "{counter}"
        mapfile -t s < "{status_file}"
        idx=$n
        [ "$idx" -ge "${{#s[@]}}" ] && idx=$(( ${{#s[@]}} - 1 ))
        echo "${{s[$idx]}}"
        exit 0 ;;
    esac ;;
esac
if [ "$1" = "exec" ]; then exit {0 if tcp_ok else 1}; fi
exit 0
"""
    )
    stub.chmod(0o755)

    env = dict(os.environ)
    env["PATH"] = f"{harness / 'bin'}{os.pathsep}{env['PATH']}"
    env["DB_CID"] = "deadbeef"
    env["DB_WAIT_ATTEMPTS"] = str(attempts)
    proc = subprocess.run(
        ["bash", str(_SCRIPT)], capture_output=True, text=True, env=env, check=False
    )
    return Result(
        returncode=proc.returncode,
        stdout=proc.stdout,
        calls=(harness / "calls.log").read_text().splitlines(),
    )


def test_no_healthcheck_skips_the_wait_entirely(harness: Path) -> None:
    result = _run(harness, statuses=["healthy"], has_healthcheck=False)

    assert result.returncode == 0
    assert result.logged("declares no healthcheck")
    assert result.sleeps == 0
    assert result.tcp_probes == 0


def test_two_consecutive_passes_are_required(harness: Path) -> None:
    result = _run(harness, statuses=["healthy"])

    assert result.returncode == 0
    assert result.logged("1/2 consecutive")
    assert result.logged("Postgres healthy and accepting TCP")
    # One pass must not be enough: on a first boot the initdb temp server can
    # answer a single probe and then disappear.
    assert result.tcp_probes == 2


def test_a_dropped_probe_resets_the_streak(harness: Path) -> None:
    # healthy, then not, then healthy twice -- the streak must restart, so the
    # run needs four attempts rather than the two a naive counter would use.
    result = _run(harness, statuses=["healthy", "starting", "healthy", "healthy"], attempts=6)

    assert result.returncode == 0
    # The "1/2 consecutive" line appears for the first pass and again after the
    # reset; a streak that survived the gap would print it only once.
    assert result.stdout.count("1/2 consecutive") == 2


def test_health_alone_is_not_enough_without_tcp(harness: Path) -> None:
    # The container healthcheck is a bare pg_isready over the local socket,
    # which the initdb temp server also answers. Only TCP separates them.
    result = _run(harness, statuses=["healthy"], attempts=3, tcp_ok=False)

    assert result.returncode == 1
    assert result.logged("did not become healthy")
    assert not result.logged("accepting TCP")


def test_the_tcp_probe_forces_a_network_connection(harness: Path) -> None:
    result = _run(harness, statuses=["healthy"])

    # -h 127.0.0.1 is the load-bearing flag: without it the probe reaches the
    # socket-only temp server and the whole distinction collapses.
    assert result.called("pg_isready -h 127.0.0.1 -p 5432")


def test_unhealthy_keeps_waiting_rather_than_failing_fast(harness: Path) -> None:
    # On a loaded host Postgres reports unhealthy for the first probes and then
    # recovers. Only the overall budget is allowed to give up.
    result = _run(harness, statuses=["unhealthy", "unhealthy", "healthy", "healthy"], attempts=6)

    assert result.returncode == 0
    assert result.logged("reports unhealthy, still waiting")
    assert result.logged("Postgres healthy and accepting TCP")


def test_the_wait_is_bounded_and_exits_nonzero_on_timeout(harness: Path) -> None:
    result = _run(harness, statuses=["starting"], attempts=4)

    assert result.returncode == 1
    assert result.logged("::error::Postgres did not become healthy within 20s")
    # Bounded: exactly the configured number of attempts, then out.
    assert result.sleeps == 4


def test_timeout_dumps_health_and_logs_for_diagnosis(harness: Path) -> None:
    result = _run(harness, statuses=["starting"], attempts=2)

    assert result.returncode == 1
    assert result.called("json .State.Health")
    assert result.called("logs --tail 200 deadbeef")


def test_an_unknown_status_is_reported_rather_than_swallowed(harness: Path) -> None:
    result = _run(harness, statuses=["starting"], attempts=1)

    assert result.logged("Postgres status: starting")


def test_script_passes_shellcheck() -> None:
    if not shutil.which("shellcheck"):
        pytest.skip("shellcheck not installed")

    proc = subprocess.run(["shellcheck", str(_SCRIPT)], capture_output=True, text=True, check=False)
    assert proc.returncode == 0, proc.stdout
