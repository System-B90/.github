"""
Name: test_hive_shared_check.py
Purpose: Regression coverage for `hive-shared.sh check`, which
         actions/shared-hive-acquire uses to decide on a bootstrap. The bug it
         pins: the baseline database vanished while state/ and the pin file
         survived, acquire skipped the bootstrap, and every job then failed in
         `ensure`. Driven through a stubbed docker on PATH; no daemon needed.
Created: 2026-10-27
Author: Michael K. Steinberg
"""

import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parents[1] / "actions" / "shared-hive" / "hive-shared.sh"

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


def _run(
    tmp_path: Path,
    *,
    dbname: bool = True,
    pin_file: bool = True,
    baseline: bool = True,
) -> Result:
    home = tmp_path / "hive-shared"
    (home / "state").mkdir(parents=True)
    (home / "stack").mkdir()
    (home / "stack" / "docker-compose.yaml").write_text("services: {}\n")
    if dbname:
        (home / "state" / "dbname").write_text("hive\n")
    if pin_file:
        (home / "stack" / "docker-compose.pin.yaml").write_text(
            "services:\n  core:\n    image: hive-shared/core:abc\n"
        )

    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    calls = tmp_path / "calls.log"
    calls.write_text("")
    (bin_dir / "sleep").write_text("#!/usr/bin/env bash\nexit 0\n")
    (bin_dir / "docker").write_text(
        f"""#!/usr/bin/env bash
echo "docker $*" >> "{calls}"
case "$*" in
  *"ps -q database"*) echo dbcid ;;
  *"State.Health.Status"*) echo healthy ;;
  *"pg_database WHERE datname="*) {"echo 1" if baseline else ":"} ;;
esac
exit 0
"""
    )
    for stub in bin_dir.iterdir():
        stub.chmod(0o755)

    env = dict(os.environ)
    env["PATH"] = f"{bin_dir}{os.pathsep}{env['PATH']}"
    env["HIVE_SHARED_HOME"] = str(home)
    env.pop("GHCR_TOKEN", None)
    proc = subprocess.run(
        ["bash", str(_SCRIPT), "check"],
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )
    return Result(proc.returncode, proc.stdout + proc.stderr, calls.read_text().splitlines())


def test_a_usable_instance_passes(tmp_path: Path) -> None:
    result = _run(tmp_path)

    assert result.returncode == 0
    assert result.called("up -d database redis")


def test_a_missing_baseline_database_fails(tmp_path: Path) -> None:
    # The regression: state/dbname and the pin file are intact, only the
    # baseline is gone. Acquire must see this as "needs bootstrap".
    result = _run(tmp_path, baseline=False)

    assert result.returncode != 0
    assert result.logged("Baseline database 'hive_ci_baseline' is missing")


def test_no_state_fails_without_touching_docker(tmp_path: Path) -> None:
    result = _run(tmp_path, dbname=False)

    assert result.returncode != 0
    assert result.calls == []


def test_an_unpinned_instance_fails(tmp_path: Path) -> None:
    result = _run(tmp_path, pin_file=False)

    assert result.returncode != 0
    assert result.calls == []
