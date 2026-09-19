"""
Name: test_publish.py
Purpose: Unit tests for scripts/publish.py -- the version-bump/tag/push tool
         every package repo in the org releases through.
Created: 2026-09-19
Author: Michael K. Steinberg
"""

import importlib.util
import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[1]


def _load_publish():
    """Imports scripts/publish.py by path -- `scripts/` is not a package."""
    spec = importlib.util.spec_from_file_location("publish", _REPO_ROOT / "scripts" / "publish.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


publish = _load_publish()


@pytest.mark.parametrize(
    ("version", "part", "expected"),
    [
        ("1.2.3", "major", "2.0.0"),
        ("1.2.3", "minor", "1.3.0"),
        ("1.2.3", "patch", "1.2.4"),
        ("0.0.0", "major", "1.0.0"),
        ("0.0.0", "minor", "0.1.0"),
        ("0.0.0", "patch", "0.0.1"),
        # Multi-digit components must not be treated as strings.
        ("9.10.11", "major", "10.0.0"),
        ("9.10.11", "minor", "9.11.0"),
        ("9.10.11", "patch", "9.10.12"),
        # A major or minor bump zeroes everything below it.
        ("1.9.9", "major", "2.0.0"),
        ("1.9.9", "minor", "1.10.0"),
    ],
)
def test_bump_matrix(version: str, part: str, expected: str) -> None:
    assert publish.bump(version, expected_part := part) == expected
    assert expected_part == part


def test_bump_treats_any_unknown_part_as_patch() -> None:
    # `main` validates the part before calling this, so the fallthrough is the
    # implicit-patch default rather than a silent accept of bad input.
    assert publish.bump("1.2.3", "patch") == "1.2.4"


PYPROJECT = """\
[project]
name = "demo"
version = "1.2.3"
description = "demo"
"""


def _git(*args: str, cwd: Path) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, text=True
    ).stdout.strip()


@pytest.fixture
def repo(tmp_path: Path) -> Iterator[Path]:
    """A real git repo on `master` with a bare remote to push into."""
    remote = tmp_path / "remote.git"
    _git("init", "--bare", "--initial-branch=master", str(remote), cwd=tmp_path)

    work = tmp_path / "work"
    work.mkdir()
    _git("init", "--initial-branch=master", cwd=work)
    _git("config", "user.email", "test@example.com", cwd=work)
    _git("config", "user.name", "Test", cwd=work)
    _git("remote", "add", "origin", str(remote), cwd=work)
    (work / "pyproject.toml").write_text(PYPROJECT)
    _git("add", ".", cwd=work)
    _git("commit", "-m", "initial", cwd=work)
    yield work


def _run_main(argv: list[str], monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(sys, "argv", ["publish.py", *argv])
    publish.main()


def test_happy_path_bumps_commits_and_tags(
    repo: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
) -> None:
    _run_main([str(repo), "minor"], monkeypatch)

    assert 'version = "1.3.0"' in (repo / "pyproject.toml").read_text()
    assert _git("log", "-1", "--pretty=%s", cwd=repo) == "Vibe-Bumped version to 1.3.0"
    assert "v1.3.0" in _git("tag", "--list", cwd=repo)
    # Annotated, not lightweight: the release workflow reads the tag message.
    assert _git("cat-file", "-t", "v1.3.0", cwd=repo) == "tag"
    assert "1.2.3 -> 1.3.0" in capsys.readouterr().out


def test_happy_path_pushes_branch_and_tag(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _run_main([str(repo), "patch"], monkeypatch)

    remote = repo.parent / "remote.git"
    assert "v1.2.4" in _git("tag", "--list", cwd=remote)
    assert _git("log", "-1", "--pretty=%s", "master", cwd=remote) == "Vibe-Bumped version to 1.2.4"


def test_part_defaults_to_patch(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _run_main([str(repo)], monkeypatch)

    assert 'version = "1.2.4"' in (repo / "pyproject.toml").read_text()


def test_missing_arguments_exits_with_usage(monkeypatch: pytest.MonkeyPatch) -> None:
    with pytest.raises(SystemExit) as excinfo:
        _run_main([], monkeypatch)

    assert "Usage:" in str(excinfo.value)


def test_invalid_part_is_rejected(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    with pytest.raises(SystemExit) as excinfo:
        _run_main([str(repo), "pathc"], monkeypatch)

    assert "part must be major|minor|patch" in str(excinfo.value)
    # Nothing was touched before the guard fired.
    assert 'version = "1.2.3"' in (repo / "pyproject.toml").read_text()


def test_refuses_a_feature_branch(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # Version bumps are the one sanctioned commit straight to master; from a
    # feature branch the tag would point at unreviewed history.
    _git("checkout", "-b", "feature/x", cwd=repo)

    with pytest.raises(SystemExit) as excinfo:
        _run_main([str(repo), "patch"], monkeypatch)

    assert "Must be on main/master" in str(excinfo.value)
    assert _git("tag", "--list", cwd=repo) == ""


def test_accepts_main_as_well_as_master(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _git("branch", "-m", "master", "main", cwd=repo)

    _run_main([str(repo), "patch"], monkeypatch)

    assert "v1.2.4" in _git("tag", "--list", cwd=repo)


def test_refuses_a_dirty_working_tree(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    (repo / "stray.txt").write_text("uncommitted")

    with pytest.raises(SystemExit) as excinfo:
        _run_main([str(repo), "patch"], monkeypatch)

    assert "Working tree not clean" in str(excinfo.value)
    assert _git("tag", "--list", cwd=repo) == ""


def test_refuses_an_unstaged_modification(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # A half-finished edit to pyproject.toml itself is the dangerous case: the
    # rewrite below would otherwise be committed along with it.
    (repo / "pyproject.toml").write_text(PYPROJECT + "\nextra = 1\n")

    with pytest.raises(SystemExit) as excinfo:
        _run_main([str(repo), "patch"], monkeypatch)

    assert "Working tree not clean" in str(excinfo.value)


def test_missing_version_line_reports_clearly(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    (repo / "pyproject.toml").write_text('[project]\nname = "demo"\n')
    _git("commit", "-am", "drop version", cwd=repo)

    with pytest.raises(SystemExit) as excinfo:
        _run_main([str(repo), "patch"], monkeypatch)

    assert 'No version = "X.Y.Z" line found' in str(excinfo.value)


def test_version_must_be_at_line_start(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # The regex is anchored with ^ under MULTILINE, so an indented or
    # commented-out version is not mistaken for the real one.
    (repo / "pyproject.toml").write_text('[project]\nname = "demo"\n  version = "1.2.3"\n')
    _git("commit", "-am", "indent version", cwd=repo)

    with pytest.raises(SystemExit) as excinfo:
        _run_main([str(repo), "patch"], monkeypatch)

    assert 'No version = "X.Y.Z" line found' in str(excinfo.value)


def test_rewrites_only_the_first_occurrence(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # A pin elsewhere in the file that happens to carry the same string must
    # survive -- `replace(..., 1)` is what protects it.
    (repo / "pyproject.toml").write_text(
        '[project]\nname = "demo"\nversion = "1.2.3"\ndependencies = ["other-pkg==1.2.3"]\n'
    )
    _git("commit", "-am", "add pin", cwd=repo)

    _run_main([str(repo), "patch"], monkeypatch)

    text = (repo / "pyproject.toml").read_text()
    assert 'version = "1.2.4"' in text
    assert "other-pkg==1.2.3" in text, "an unrelated pin must not be bumped"


def test_commits_only_pyproject(repo: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # `git add pyproject.toml` is deliberately narrow, but the clean-tree guard
    # means nothing else should be pending anyway. This pins both.
    _run_main([str(repo), "patch"], monkeypatch)

    changed = _git("show", "--name-only", "--pretty=", "HEAD", cwd=repo)
    assert changed == "pyproject.toml"
