"""
Name: test_teardown_stack.py
Purpose: Branch coverage for actions/teardown-hive/teardown-stack.sh, driven
         through a stubbed docker on PATH. No Docker daemon is required and
         nothing real is torn down.
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

_SCRIPT = Path(__file__).resolve().parents[1] / "actions" / "teardown-hive" / "teardown-stack.sh"

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


@pytest.fixture
def harness(tmp_path: Path) -> Iterator[Path]:
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (tmp_path / "calls.log").write_text("")
    yield tmp_path


def _run(
    harness: Path,
    *,
    compose_file: bool,
    leftovers: tuple[str, ...] = (),
    compose_down_exit: int = 0,
) -> Result:
    hive = harness / "hive"
    hive.mkdir(exist_ok=True)
    if compose_file:
        (hive / "docker-compose.yaml").write_text("services: {}\n")

    # One docker stub serves every call the script makes. `ps -aq` is the only
    # one whose output the script branches on, so it is the only one modelled.
    listing = "\n".join(leftovers)
    stub = harness / "bin" / "docker"
    stub.write_text(
        f"""#!/usr/bin/env bash
echo "docker $*" >> "{harness}/calls.log"
if [ "$1 $2 $3" = "ps -aq --filter" ]; then
  printf '%s' "{listing}"
  [ -n "{listing}" ] && echo
  exit 0
fi
if [ "$1" = "compose" ]; then exit {compose_down_exit}; fi
exit 0
"""
    )
    stub.chmod(0o755)

    env = dict(os.environ)
    env["PATH"] = f"{harness / 'bin'}{os.pathsep}{env['PATH']}"
    env["HIVE_PATH"] = str(hive)
    proc = subprocess.run(
        ["bash", str(_SCRIPT)], capture_output=True, text=True, env=env, check=False
    )
    return Result(
        returncode=proc.returncode,
        stdout=proc.stdout,
        calls=(harness / "calls.log").read_text().splitlines(),
    )


def test_composes_down_with_volumes_and_orphans(harness: Path) -> None:
    result = _run(harness, compose_file=True)

    assert result.returncode == 0
    # -v and --remove-orphans are the reason this step reclaims anything at
    # all; dropping either turns teardown into a no-op that still reads green.
    assert result.called("compose -f")
    assert result.called("down -v --remove-orphans")


def test_missing_compose_file_skips_the_down_but_still_sweeps(harness: Path) -> None:
    result = _run(harness, compose_file=False, leftovers=("hive-core",))

    assert result.returncode == 0
    assert result.logged("nothing to compose-down")
    assert not result.called("down -v")
    # The sweep is the whole point when compose cannot help: a stack brought up
    # from a since-deleted workspace has no project file left to describe it.
    assert result.called("rm -f hive-core")


def test_leftover_containers_are_force_removed(harness: Path) -> None:
    result = _run(harness, compose_file=True, leftovers=("hive-core", "hive-nginx"))

    assert result.returncode == 0
    assert result.logged("Removing leftover hive-* containers")
    assert result.called("rm -f hive-core hive-nginx")


def test_no_leftovers_means_no_rm(harness: Path) -> None:
    result = _run(harness, compose_file=True)

    assert result.returncode == 0
    assert not result.called("rm -f")
    assert not result.logged("Removing leftover")


def test_the_filter_is_anchored_to_the_hive_prefix(harness: Path) -> None:
    result = _run(harness, compose_file=True, leftovers=("hive-core",))

    # `^/hive-` rather than `hive`: an unanchored filter would also match a
    # sibling job's container whose name merely contains "hive". Asserted on
    # every call that carries a filter, so anchoring one and not the other
    # cannot pass.
    filtered = [call for call in result.calls if "--filter" in call]
    assert filtered
    assert all("--filter name=^/hive-" in call for call in filtered)


def test_a_failing_compose_down_does_not_fail_the_job(harness: Path) -> None:
    # A cleanup error must never turn a green run red -- the action is
    # documented as never failing, and consumers call it with `if: always()`.
    result = _run(harness, compose_file=True, compose_down_exit=1, leftovers=("hive-core",))

    assert result.returncode == 0
    # And it must keep going: the sweep still runs after the failed down.
    assert result.called("rm -f hive-core")


def test_stopped_containers_are_still_removed(harness: Path) -> None:
    # `ps -aq`, not `ps -q`: a stack killed mid-bring-up leaves *exited*
    # containers, and those still hold bind-mounted data files open.
    result = _run(harness, compose_file=True, leftovers=("hive-database",))

    assert result.called("ps -aq")
    assert result.called("rm -f hive-database")


def test_script_passes_shellcheck() -> None:
    if not shutil.which("shellcheck"):
        pytest.skip("shellcheck not installed")

    proc = subprocess.run(["shellcheck", str(_SCRIPT)], capture_output=True, text=True, check=False)
    assert proc.returncode == 0, proc.stdout
