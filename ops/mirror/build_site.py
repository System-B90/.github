"""
Name: build_site.py
Purpose: Stages the Docker build context of the System-B90 offline mirror
         (System-B90/.github#42): the org pip index plus the dependency closure
         of every package on it, the docs sites, and the plugin marketplace.
         The Dockerfile beside this script bakes the result into one nginx
         image. See README.md.
Created: 2026-10-27
Author: Michael K. Steinberg
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent

# Every published page and plugin points here. nginx rewrites it to the
# mirror's own address on the way out (nginx.conf), and 40-marketplace.sh does
# the same inside the marketplace git repo, so neither is rewritten at build.
PAGES_URL = "https://system-b90.github.io/.github"
DOC_SITES = ("bluz", "pyhive")
PYPI_TOOLING = {"README.md", "generate_index.py"}
CONTEXT_FILES = ("Dockerfile", "nginx.conf", "40-marketplace.sh")
# Lets an air-gapped host build an sdist or upgrade its own pip.
BASE_SEED = "pip\nsetuptools\nwheel\n"


def normalize(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def dist_project(filename: str) -> str:
    """PEP 503 project name of a wheel or sdist filename."""
    return normalize(filename.split("-")[0])


def stage_pypi(site: Path, repo: Path = REPO) -> list[str]:
    """Copies the org's own distributions. Returns the org project names."""
    target = site / "pypi"
    projects = []
    for entry in sorted((repo / "pypi").iterdir()):
        if entry.is_dir() and not entry.name.startswith("."):
            shutil.copytree(entry, target / entry.name)
            projects.append(entry.name)
        elif entry.name not in PYPI_TOOLING and entry.name != "index.html":
            raise SystemExit(f"unexpected file in pypi/: {entry.name}")
    return projects


def place(wheels: Path, pypi: Path) -> int:
    """Files each wheel under its project; keeps the org's own copies."""
    added = 0
    for wheel in sorted(wheels.glob("*.whl")):
        destination = pypi / dist_project(wheel.name) / wheel.name
        if destination.exists():
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(wheel), destination)
        added += 1
    return added


def version_key(filename: str) -> tuple:
    """Orders `name-1.10.0rc2-...` releases: numerically, finals after their rcs."""
    match = re.match(r"[^-]+-(\d+(?:\.\d+)*)(?:(a|b|rc)(\d+))?[-.]", filename)
    if not match:
        raise SystemExit(f"cannot read a version from {filename}")
    release = tuple(int(part) for part in match.group(1).split("."))
    pre = (0, match.group(2), int(match.group(3))) if match.group(2) else (1, "", 0)
    return release, pre


def latest_wheel(project_dir: Path) -> Path | None:
    wheels = list(project_dir.glob("*.whl"))
    return max(wheels, key=lambda w: version_key(w.name)) if wheels else None


def requires_python(wheel: Path) -> str:
    with zipfile.ZipFile(wheel) as archive:
        metadata = next(n for n in archive.namelist() if n.endswith(".dist-info/METADATA"))
        for line in archive.read(metadata).decode("utf-8").splitlines():
            if line.startswith("Requires-Python:"):
                return line.split(":", 1)[1].strip()
            if not line:
                break
    return ""


def supports(specifier: str, python: str) -> bool:
    """Whether a Requires-Python like `>=3.10.0,<4` admits Python `3.N`."""
    have = tuple(int(part) for part in python.split("."))
    compare = {
        ">=": lambda a, b: a >= b,
        ">": lambda a, b: a > b,
        "<=": lambda a, b: a <= b,
        "<": lambda a, b: a < b,
        "==": lambda a, b: a == b,
        "!=": lambda a, b: a != b,
    }
    for clause in filter(None, (c.strip() for c in specifier.split(","))):
        match = re.fullmatch(r"(>=|<=|==|!=|>|<)\s*(\d+(?:\.\d+)*)(?:\.\*)?", clause)
        if not match:
            raise SystemExit(f"unsupported Requires-Python clause: {clause!r}")
        # Compare at minor precision: `>=3.10.0` admits 3.10, `<3.11.2` admits 3.11.
        want = tuple(int(part) for part in match.group(2).split("."))[:2]
        if not compare[match.group(1)](have, want):
            return False
    return True


def add_dependencies(pypi: Path, projects: list[str], index: str) -> None:
    """The latest release of every org project, with everything it needs, for
    every platform and every Python an app bundle targets that the release
    itself supports (bluz needs 3.11+, so it gets no 3.10 set).

    Resolution is sb90-deploy's own (uv per target, then pip download), strict
    the same way: a dependency without a wheel for some target fails here, not
    on an air-gapped host. One resolve per project, because old releases of
    renamed packages (bluz-cli) need not agree with the current ones.
    """
    from sb90_deploy.bundle import DEFAULT_PLATFORMS, DEFAULT_PYTHONS, download_wheels

    seeds = [("base", BASE_SEED, list(DEFAULT_PYTHONS))]
    for name in projects:
        wheel = latest_wheel(pypi / name)
        if wheel is None:
            print(f"[mirror] {name}: no wheels, nothing to resolve")
            continue
        version = wheel.name.split("-")[1]
        specifier = requires_python(wheel)
        pythons = [p for p in DEFAULT_PYTHONS if supports(specifier, p)]
        seeds.append((f"{name}=={version}", f"{name}=={version}\n", pythons))
    for label, requirement, pythons in seeds:
        with tempfile.TemporaryDirectory() as tmp:
            requirements = Path(tmp) / "requirements.txt"
            requirements.write_text(requirement)
            wheels = Path(tmp) / "wheels"
            wheels.mkdir()
            download_wheels(requirements, wheels, DEFAULT_PLATFORMS, pythons, index)
            added = place(wheels, pypi)
            print(f"[mirror] {label} (Python {', '.join(pythons)}): {added} new wheels")


def write_indexes(pypi: Path, repo: Path = REPO) -> None:
    """The repo's own generator, run over the staged tree, then dropped."""
    generator = pypi / "generate_index.py"
    shutil.copy2(repo / "pypi" / "generate_index.py", generator)
    subprocess.run([sys.executable, str(generator)], check=True)
    generator.unlink()


def stage_docs(site: Path, repo: Path = REPO) -> list[str]:
    staged = []
    for name in DOC_SITES:
        if (repo / name).is_dir():
            shutil.copytree(repo / name, site / name)
            staged.append(name)
    return staged


def stage_marketplace(out: Path, repo: Path = REPO) -> None:
    """Served as a git repo, built at container start (40-marketplace.sh)."""
    marketplace = out / "marketplace"
    shutil.copytree(repo / ".claude-plugin", marketplace / ".claude-plugin")
    shutil.copytree(repo / "plugins", marketplace / "plugins")


def landing_page(tag: str, projects: list[str], docs: list[str]) -> str:
    # Written with PAGES_URL like every other page, so the same nginx rewrite
    # turns it into whatever address the reader used.
    packages = "".join(f"<li><code>{html.escape(p)}</code></li>" for p in projects)
    doc_links = "".join(f'<li><a href="{d}/">{d}</a></li>' for d in docs)
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>System-B90 mirror</title>
<style>body{{font-family:system-ui,sans-serif;max-width:46rem;margin:2rem auto;padding:0 1rem;line-height:1.5}}
pre{{background:#f4f4f4;padding:.75rem;overflow-x:auto}}</style></head>
<body>
<h1>System-B90 mirror</h1>
<p>Offline copy of the org's pip index, Claude Code plugins and docs. Release <code>{html.escape(tag)}</code>.</p>

<h2>Trust this mirror</h2>
<p>Its certificate is signed by the mirror's own CA. Download <a href="ca.crt">ca.crt</a>, then on Linux:</p>
<pre>pip config set global.cert /path/to/ca.crt
git config --global http.{PAGES_URL}/.sslCAInfo /path/to/ca.crt</pre>
<p>On Windows, git checks the Windows certificate store and ignores <code>sslCAInfo</code>, so add the CA there, and point pip at it:</p>
<pre>certutil -addstore -user Root ca.crt
pip config set global.cert C:\\path\\to\\ca.crt</pre>

<h2>pip</h2>
<p>Each package below installs with all of its dependencies, for Python 3.10&ndash;3.13 on Linux and Windows.</p>
<pre>pip install bluz --index-url {PAGES_URL}/pypi/</pre>
<ul>{packages}</ul>

<h2>Claude Code plugins</h2>
<pre>/plugin marketplace add {PAGES_URL}/marketplace.git
/plugin install bluz@system-b90-marketplace</pre>

<h2>Docs</h2>
<ul>{doc_links}</ul>
</body>
</html>
"""


def build(out: Path, tag: str, deps: bool, index: str, repo: Path = REPO) -> None:
    if out.exists():
        shutil.rmtree(out)
    site = out / "site"
    site.mkdir(parents=True)
    projects = stage_pypi(site, repo)
    if deps:
        add_dependencies(site / "pypi", projects, index)
    write_indexes(site / "pypi", repo)
    docs = stage_docs(site, repo)
    stage_marketplace(out, repo)
    (site / "index.html").write_text(landing_page(tag, projects, docs), encoding="utf-8")
    for name in CONTEXT_FILES:
        shutil.copy2(HERE / name, out / name)
    print(f"[mirror] staged {out} ({len(projects)} org packages, docs: {', '.join(docs) or '-'})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("out", type=Path, help="build context to (re)create")
    parser.add_argument("--tag", required=True, help="release tag shown on the landing page")
    parser.add_argument(
        "--no-deps", action="store_true", help="org packages only (fast; not usable offline)"
    )
    parser.add_argument("--index", default=PAGES_URL + "/pypi/", help="org pip index")
    args = parser.parse_args()
    build(args.out, args.tag, not args.no_deps, args.index)


if __name__ == "__main__":
    main()
