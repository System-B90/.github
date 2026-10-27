"""
Name: test_mirror.py
Purpose: The offline mirror (ops/mirror, #42): build_site.py's version and
    Requires-Python handling, the staged build context, and the release
    description agreeing with itself. Dependency resolution needs the network
    and sb90-deploy, so it is covered by the release workflow, not here.
Created: 2026-10-27
Author: Michael K. Steinberg
"""

import importlib.util
import json
import re
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
MIRROR = ROOT / "ops" / "mirror"

_spec = importlib.util.spec_from_file_location("build_site", MIRROR / "build_site.py")
build_site = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_site)


def _wheel(directory: Path, name: str, requires_python: str = "") -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / name
    project, version = name.split("-")[:2]
    metadata = f"Metadata-Version: 2.1\nName: {project}\nVersion: {version}\n"
    if requires_python:
        metadata += f"Requires-Python: {requires_python}\n"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(
            f"{project}-{version}.dist-info/METADATA", metadata + "\nlong description\n"
        )
    return path


@pytest.mark.parametrize(
    ("filename", "project"),
    [
        ("bluz_cli-1.3.3-py3-none-any.whl", "bluz-cli"),
        ("PyHiveLMS-3.1.0-py3-none-any.whl", "pyhivelms"),
        ("sb90_deploy-0.6.0.tar.gz", "sb90-deploy"),
    ],
)
def test_dist_project_is_the_pep503_name(filename: str, project: str) -> None:
    assert build_site.dist_project(filename) == project


def test_latest_wheel_orders_numerically_and_finals_after_rcs(tmp_path: Path) -> None:
    for name in (
        "bluz-1.9.0-py3-none-any.whl",
        "bluz-1.10.0rc2-py3-none-any.whl",
        "bluz-1.10.0-py3-none-any.whl",
        "bluz-1.10.0rc11-py3-none-any.whl",
    ):
        _wheel(tmp_path, name)
    # Lexical order would pick 1.9.0, or an rc over its final.
    assert build_site.latest_wheel(tmp_path).name == "bluz-1.10.0-py3-none-any.whl"


def test_latest_wheel_is_none_without_wheels(tmp_path: Path) -> None:
    assert build_site.latest_wheel(tmp_path) is None


def test_requires_python_is_read_from_the_wheel(tmp_path: Path) -> None:
    wheel = _wheel(tmp_path, "bluz-1.8.1-py3-none-any.whl", ">=3.11")
    assert build_site.requires_python(wheel) == ">=3.11"
    assert build_site.requires_python(_wheel(tmp_path, "x-1.0.0-py3-none-any.whl")) == ""


@pytest.mark.parametrize(
    ("specifier", "admitted"),
    [
        ("", ["3.10", "3.11", "3.12", "3.13"]),
        (">=3.11", ["3.11", "3.12", "3.13"]),
        (">=3.10.0", ["3.10", "3.11", "3.12", "3.13"]),
        (">=3.10, <3.13", ["3.10", "3.11", "3.12"]),
        ("!=3.12.*", ["3.10", "3.11", "3.13"]),
        ("<4", ["3.10", "3.11", "3.12", "3.13"]),
    ],
)
def test_supports_filters_target_pythons(specifier: str, admitted: list[str]) -> None:
    targets = ["3.10", "3.11", "3.12", "3.13"]
    assert [p for p in targets if build_site.supports(specifier, p)] == admitted


def test_supports_refuses_what_it_cannot_read() -> None:
    with pytest.raises(SystemExit):
        build_site.supports("~=3.10", "3.11")


def test_place_files_wheels_by_project_and_keeps_existing(tmp_path: Path) -> None:
    pypi = tmp_path / "pypi"
    existing = _wheel(pypi / "pyhivelms", "pyhivelms-3.1.0-py3-none-any.whl")
    existing.write_bytes(b"org copy")
    downloads = tmp_path / "downloads"
    _wheel(downloads, "pyhivelms-3.1.0-py3-none-any.whl")
    _wheel(downloads, "httpx-0.28.1-py3-none-any.whl")

    assert build_site.place(downloads, pypi) == 1
    assert (pypi / "httpx" / "httpx-0.28.1-py3-none-any.whl").is_file()
    assert existing.read_bytes() == b"org copy"


@pytest.fixture
def fake_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    (repo / "pypi").mkdir(parents=True)
    (repo / "pypi" / "generate_index.py").write_bytes(
        (ROOT / "pypi" / "generate_index.py").read_bytes()
    )
    (repo / "pypi" / "README.md").write_text("tooling\n")
    (repo / "pypi" / "index.html").write_text("stale\n")
    _wheel(repo / "pypi" / "bluz", "bluz-1.8.1-py3-none-any.whl", ">=3.11")
    (repo / "bluz").mkdir()
    (repo / "bluz" / "index.html").write_text("docs\n")
    (repo / ".claude-plugin").mkdir()
    (repo / ".claude-plugin" / "marketplace.json").write_text("{}\n")
    (repo / "plugins" / "bluz").mkdir(parents=True)
    (repo / "plugins" / "bluz" / "hook.js").write_text(f'"{build_site.PAGES_URL}/pypi/"\n')
    return repo


def test_build_stages_a_complete_context(tmp_path: Path, fake_repo: Path) -> None:
    out = tmp_path / "ctx"
    build_site.build(out, "v2026.10.27", deps=False, index="unused", repo=fake_repo)

    pypi = out / "site" / "pypi"
    assert "bluz/" in (pypi / "index.html").read_text()
    assert "bluz-1.8.1-py3-none-any.whl" in (pypi / "bluz" / "index.html").read_text()
    # The index's own tooling is not part of the served site.
    assert not (pypi / "generate_index.py").exists()
    assert not (pypi / "README.md").exists()

    assert (out / "site" / "bluz" / "index.html").is_file()
    assert not (out / "site" / "pyhive").exists()
    assert (out / "marketplace" / ".claude-plugin" / "marketplace.json").is_file()
    # The rewrite happens at container start, against the real address.
    assert (
        build_site.PAGES_URL in (out / "marketplace" / "plugins" / "bluz" / "hook.js").read_text()
    )

    landing = (out / "site" / "index.html").read_text(encoding="utf-8")
    assert "v2026.10.27" in landing
    assert f"{build_site.PAGES_URL}/marketplace.git" in landing
    for name in build_site.CONTEXT_FILES:
        assert (out / name).is_file()


def test_build_refuses_unknown_files_in_pypi(tmp_path: Path, fake_repo: Path) -> None:
    (fake_repo / "pypi" / "stray.whl").write_text("")
    with pytest.raises(SystemExit):
        build_site.build(tmp_path / "ctx", "v0.0.0", deps=False, index="unused", repo=fake_repo)


def test_nginx_never_serves_the_private_keys() -> None:
    conf = (MIRROR / "nginx.conf").read_text(encoding="utf-8")
    # ssl/ holds ca.key and key.pem next to ca.crt: only the one file is aliased.
    assert re.findall(r"^\s*alias\s+(\S+);", conf, re.MULTILINE) == ["/etc/nginx/ssl/ca.crt"]
    assert "root /srv/www;" in conf


def test_release_description_agrees_with_itself() -> None:
    app = json.loads((MIRROR / "app.json").read_text(encoding="utf-8"))
    compose = (MIRROR / "docker-compose.release.yml").read_text(encoding="utf-8")

    assert f"${{{app['env_prefix']}_VERSION:?" in compose
    for prefix_var in ("BIND_IP", "HTTP_PORT", "HTTPS_PORT"):
        assert f"${{{app['env_prefix']}_{prefix_var}" in compose
    for service in app["roll"] + [app["health"]["service"]]:
        assert re.search(rf"^  {service}:$", compose, re.MULTILINE)
    for container in app["containers"].values():
        assert f"container_name: {container}" in compose
    for source in app["bundle"]["files"].values():
        assert (ROOT / source).is_file()
    assert "- ./ssl:/etc/nginx/ssl:ro" in compose and app["state"] == ["ssl"]

    workflow = (ROOT / ".github" / "workflows" / "mirror-release.yml").read_text(encoding="utf-8")
    image = re.search(r"image: (\S+):\$\{", compose).group(1)
    assert f"IMAGE: {image}:${{{{ steps.tag.outputs.tag }}}}" in workflow
