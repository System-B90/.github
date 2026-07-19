"""Regenerates the PEP 503 simple index under pypi/ from the .whl/.tar.gz files on disk.

Run after copying new distributions into pypi/<package>/. No third-party deps.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PYPI_ROOT = Path(__file__).parent


def normalize(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def package_dist_name(filename: str) -> str:
    return filename.split("-")[0]


def generate_package_index(package_dir: Path) -> None:
    dist_files = sorted(
        f for f in package_dir.iterdir() if f.suffix in (".whl", ".gz") and f.name != "index.html"
    )
    links = "\n".join(f'    <a href="{f.name}">{f.name}</a><br/>' for f in dist_files)
    (package_dir / "index.html").write_text(
        f"<!DOCTYPE html>\n<html>\n  <body>\n{links}\n  </body>\n</html>\n"
    )


def generate_root_index() -> None:
    package_dirs = sorted(
        d for d in PYPI_ROOT.iterdir() if d.is_dir() and not d.name.startswith(".")
    )
    links = "\n".join(f'    <a href="{d.name}/">{d.name}</a><br/>' for d in package_dirs)
    (PYPI_ROOT / "index.html").write_text(
        f"<!DOCTYPE html>\n<html>\n  <body>\n{links}\n  </body>\n</html>\n"
    )


def main() -> None:
    package_name = normalize(sys.argv[1]) if len(sys.argv) > 1 else None
    package_dirs = (
        [PYPI_ROOT / package_name] if package_name else [d for d in PYPI_ROOT.iterdir() if d.is_dir()]
    )
    for package_dir in package_dirs:
        generate_package_index(package_dir)
    generate_root_index()


if __name__ == "__main__":
    main()
