"""
Name: test_ci_disk_reclaim.py
Purpose: Branch coverage for ops/runner/ci-disk-reclaim.sh, driven through
         stubbed docker/df/journalctl/logger/stat binaries on PATH. Nothing
         real is pruned and no Docker daemon is required.
Created: 2026-09-19
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

_SCRIPT = Path(__file__).resolve().parents[1] / "ops" / "runner" / "ci-disk-reclaim.sh"

pytestmark = pytest.mark.skipif(
    sys.platform == "win32", reason="bash script; the runner leg that matters is Linux"
)


@dataclass
class Result:
    returncode: int
    stdout: str
    calls: list[str]

    def logged(self, needle: str) -> bool:
        return any(needle in line for line in self.stdout.splitlines())

    def called(self, needle: str) -> bool:
        return any(needle in call for call in self.calls)


def _write_stub(path: Path, body: str) -> None:
    path.write_text(f"#!/usr/bin/env bash\n{body}\n")
    path.chmod(0o755)


@pytest.fixture
def harness(tmp_path: Path) -> Iterator[Path]:
    """A bin/ dir of stubs that record their argv into calls.log."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (tmp_path / "calls.log").write_text("")

    record = f'echo "$(basename "$0") $*" >> "{tmp_path}/calls.log"'

    # `timeout` is real on Linux but would need the stubs on PATH anyway;
    # passing through keeps the script's own timeout wrappers exercised.
    _write_stub(bin_dir / "logger", record)
    _write_stub(bin_dir / "journalctl", f"{record}\nexit 0")
    _write_stub(bin_dir / "stat", f"{record}\necho 0")
    yield tmp_path


def _run(
    harness: Path,
    *,
    free_before: int,
    free_after: int | None = None,
    docker_body: str = "exit 0",
) -> Result:
    """Runs the script with df reporting `free_before` then `free_after` GB."""
    bin_dir = harness / "bin"
    after = free_before if free_after is None else free_after
    counter = harness / "df.count"
    counter.write_text("0")
    # df is called once up front and once at the end; the counter lets a test
    # model "reclaim helped" and "reclaim did not help" separately.
    _write_stub(
        bin_dir / "df",
        f'''n=$(cat "{counter}")
echo $((n + 1)) > "{counter}"
echo "Avail"
if [ "$n" -eq 0 ]; then echo "{free_before}G"; else echo "{after}G"; fi''',
    )
    _write_stub(
        bin_dir / "docker",
        f'echo "docker $*" >> "{harness}/calls.log"\n{docker_body}',
    )

    env = dict(os.environ)
    env["PATH"] = f"{bin_dir}{os.pathsep}{env['PATH']}"
    env["FLOOR_GB"] = "30"
    proc = subprocess.run(
        ["bash", str(_SCRIPT)], capture_output=True, text=True, env=env, check=False
    )
    return Result(
        returncode=proc.returncode,
        stdout=proc.stdout,
        calls=(harness / "calls.log").read_text().splitlines(),
    )


def test_above_floor_does_nothing(harness: Path) -> None:
    result = _run(harness, free_before=100)

    assert result.returncode == 0
    assert result.logged("ok: 100GB free")
    # The critical property: a healthy host never has its cache pruned.
    assert not result.called("docker prune")
    assert not result.called("docker builder")
    assert not result.called("docker image prune")


def test_exactly_at_the_floor_is_treated_as_healthy(harness: Path) -> None:
    # The comparison is -ge, so the floor itself is "ok".
    result = _run(harness, free_before=30)

    assert result.returncode == 0
    assert result.logged("ok: 30GB free")
    assert not result.called("docker builder")


def test_below_floor_runs_the_reclaim_sequence_in_order(harness: Path) -> None:
    result = _run(harness, free_before=5, free_after=80)

    assert result.returncode == 0
    assert result.logged("low: 5GB free")

    order = [
        c for c in result.calls if c.startswith(("docker builder", "docker image", "journalctl"))
    ]
    # Cheapest-to-rebuild first: build cache, then images, then journals.
    assert order[0].startswith("docker builder prune")
    assert order[1].startswith("docker image prune")
    assert any(c.startswith("journalctl") for c in result.calls)


def test_reclaim_passes_its_configured_limits(harness: Path) -> None:
    result = _run(harness, free_before=5, free_after=80)

    assert result.called("--reserved-space 10GB")
    assert result.called("until=6h")
    assert result.called("--vacuum-size=200M")


def test_a_failing_builder_prune_warns_and_continues(harness: Path) -> None:
    # Only the builder prune fails; the rest of the sequence must still run.
    result = _run(
        harness,
        free_before=5,
        free_after=80,
        docker_body='case "$1 $2" in "builder prune") exit 1 ;; *) exit 0 ;; esac',
    )

    assert result.returncode == 0
    assert result.logged("WARN: builder prune failed")
    assert result.called("docker image prune")


def test_a_failing_image_prune_warns_and_continues(harness: Path) -> None:
    result = _run(
        harness,
        free_before=5,
        free_after=80,
        docker_body='case "$1 $2" in "image prune") exit 1 ;; *) exit 0 ;; esac',
    )

    assert result.returncode == 0
    assert result.logged("WARN: image prune failed")
    assert result.logged("done: 5GB -> 80GB free")


def test_still_below_floor_alerts_and_exits_nonzero(harness: Path) -> None:
    # Growth that is not regenerable Docker state needs a human, and must be
    # loud rather than silently ineffective -- this is System-B90/.github#12.
    result = _run(harness, free_before=5, free_after=8)

    assert result.returncode == 1
    assert result.logged("ALERT: still below floor after reclaim")
    assert result.logged("8GB < 30GB")


def test_recovering_above_the_floor_exits_zero(harness: Path) -> None:
    result = _run(harness, free_before=5, free_after=45)

    assert result.returncode == 0
    assert not result.logged("ALERT")


def test_dangling_volume_pass_only_removes_old_dangling_volumes(
    harness: Path,
) -> None:
    result = _run(
        harness,
        free_before=5,
        free_after=80,
        docker_body="""case "$1 $2" in
  "volume ls") echo "vol-old" ;;
  "volume inspect") echo "/var/lib/docker/volumes/vol-old/_data" ;;
esac
exit 0""",
    )

    # dangling=true is Docker's own "attached to no container" filter -- the
    # guard that keeps a live Hive stack's Postgres data safe.
    assert result.called("volume ls -q --filter dangling=true")
    assert result.logged("dangling volume(s) older than 6h")


def test_runners_without_an_inner_daemon_are_skipped(harness: Path) -> None:
    result = _run(
        harness,
        free_before=5,
        free_after=80,
        docker_body="""case "$1 $2 $3" in
  "ps --filter name=runner") echo "light-runner" ; exit 0 ;;
esac
case "$*" in
  *"exec light-runner docker info"*) exit 1 ;;
esac
exit 0""",
    )

    assert result.returncode == 0
    # The probe ran, but no prune followed it.
    assert result.called("exec light-runner docker info")
    assert not result.called("exec light-runner  docker image prune")


def test_inner_prune_failure_warns_with_the_last_output_line(
    harness: Path,
) -> None:
    # A bare "it failed" is not actionable: the runner is ephemeral and gone by
    # the time anyone reads the journal, so the output is captured.
    result = _run(
        harness,
        free_before=5,
        free_after=80,
        docker_body="""case "$1 $2 $3" in
  "ps --filter name=runner") echo "dind-runner" ; exit 0 ;;
esac
case "$*" in
  *"exec dind-runner docker info"*) exit 0 ;;
  *"image prune"*) echo "cannot connect to daemon" ; exit 1 ;;
esac
exit 0""",
    )

    assert result.logged("WARN: inner prune failed in dind-runner")
    assert result.logged("cannot connect to daemon")


def test_free_gb_parses_the_df_suffix(harness: Path) -> None:
    # free_gb() strips everything but digits, so the trailing "G" and the
    # header line must not leak into the arithmetic comparison.
    result = _run(harness, free_before=100)

    assert result.returncode == 0
    assert result.logged("ok: 100GB free")


def test_script_passes_shellcheck() -> None:
    if not shutil.which("shellcheck"):
        pytest.skip("shellcheck not installed")

    proc = subprocess.run(["shellcheck", str(_SCRIPT)], capture_output=True, text=True, check=False)
    assert proc.returncode == 0, proc.stdout
