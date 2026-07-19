#!/usr/bin/env python3
"""Bump version, commit, tag, push — target repo's CI does the rest (build, GitHub Release, pip index update).

Usage: python publish.py <path-to-repo> [major|minor|patch]   (default: patch)
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


def run(*args: str, cwd: Path) -> str:
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def bump(version: str, part: str) -> str:
    major, minor, patch = (int(x) for x in version.split("."))
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    repo = Path(sys.argv[1]).resolve()
    part = sys.argv[2] if len(sys.argv) > 2 else "patch"
    if part not in ("major", "minor", "patch"):
        sys.exit(f"part must be major|minor|patch, got '{part}'")

    pyproject = repo / "pyproject.toml"
    text = pyproject.read_text()
    match = re.search(r'^version = "(\d+\.\d+\.\d+)"', text, re.MULTILINE)
    if not match:
        sys.exit('No version = "X.Y.Z" line found in pyproject.toml')
    old_version = match.group(1)
    new_version = bump(old_version, part)

    branch = run("git", "branch", "--show-current", cwd=repo)
    if branch not in ("main", "master"):
        sys.exit(f"Must be on main/master to publish (version-bump commits skip the PR flow), currently on '{branch}'")
    if run("git", "status", "--porcelain", cwd=repo):
        sys.exit("Working tree not clean, commit or stash first")

    pyproject.write_text(text.replace(f'version = "{old_version}"', f'version = "{new_version}"', 1))
    run("git", "add", "pyproject.toml", cwd=repo)
    run("git", "commit", "-m", f"Vibe-Bumped version to {new_version}", cwd=repo)
    run("git", "push", "origin", branch, cwd=repo)
    run("git", "tag", "-a", f"v{new_version}", "-m", f"v{new_version}", cwd=repo)
    run("git", "push", "origin", f"v{new_version}", cwd=repo)

    print(f"{old_version} -> {new_version}. Tag v{new_version} pushed — CI will build, cut the GitHub Release, and update the pip index.")


if __name__ == "__main__":
    main()
