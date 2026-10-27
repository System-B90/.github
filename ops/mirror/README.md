# System-B90 offline mirror

One container that gives an air-gapped network what `https://system-b90.github.io/.github/`
gives the internet (#42):

| Path | What | Use it |
| --- | --- | --- |
| `/pypi/` | The org pip index **plus every dependency** of the latest release of each package, for Python 3.10–3.13 on Linux x86_64 and Windows x64 | `pip install bluz --index-url https://<mirror>/pypi/` |
| `/marketplace.git` | The Claude Code plugin marketplace, as a git repo | `/plugin marketplace add https://<mirror>/marketplace.git` |
| `/bluz/`, `/pyhive/` | The docs sites | browser |
| `/ca.crt` | The mirror's CA certificate | trust it once per client |
| `/` | Landing page with all the commands above, already pointing at this mirror | browser |

Every page, skill and plugin hook that names the GitHub Pages address is
pointed at the mirror's own address instead. So the plugins' `SessionStart`
hooks install their CLIs from the mirror, with no extra configuration.

It is released and installed exactly like Bluz, madash and peek-a-boo, through
`sb90-deploy`.

## Install (air-gapped host)

Needs Docker with Compose, and Python 3.10+ (Ubuntu 22.04's stock `python3` will do). On another machine, download
`sb90-mirror-offline-<tag>.tar.gz` from this repo's
[releases](https://github.com/System-B90/.github/releases) and carry it over.
Then:

```bash
tar -xzf sb90-mirror-offline-<tag>.tar.gz
cd sb90-mirror
./install.sh            # .\install.ps1 on Windows
```

The wizard asks for the mirror's domain name and ports, then issues a TLS
certificate from a CA it creates in `ssl/`. That CA is what clients trust
(`/ca.crt`; the landing page has the per-OS commands). Re-run the wizard with
`python3 bootstrap.py setup`.

## Upgrade

A release is a snapshot of `main`, so a newer one carries newer packages,
plugins and docs. Download the newer offline bundle and run:

```bash
./update.sh --package /path/to/sb90-mirror-offline-<newer-tag>.tar.gz
```

## Cutting a release

Run the **Mirror release** workflow (`.github/workflows/mirror-release.yml`)
from `main`. The tag defaults to today's date as `vYYYY.M.D`. It stages the
site (`build_site.py`), builds and pushes `ghcr.io/system-b90/mirror/web:<tag>`,
crafts the online/offline bundles with `actions/craft-release`, and publishes
the GitHub release.

Dependency resolution is strict, the same way app bundles are. If some
dependency stops publishing a wheel for one of the targets, the release fails
in CI rather than on an air-gapped host. Each package resolves only for the
Pythons its own `Requires-Python` admits, so `bluz` (3.11+) gets no 3.10 set.

## How it works

| File | Role |
| --- | --- |
| `build_site.py` | Stages the Docker build context: copies `pypi/`, resolves dependencies with sb90-deploy's own vendoring, regenerates the indexes, copies the docs and the marketplace, writes the landing page. `--no-deps` for a quick local look. |
| `Dockerfile` | `nginx:alpine` plus git, git-http-backend and fcgiwrap (serving the marketplace) and node (sb90-deploy's post-upgrade health check runs `node -e fetch(...)` in the container). |
| `40-marketplace.sh` | Runs at container start: rewrites the Pages address to `MIRROR_URL` in the plugins, commits them as a git repo with fixed dates (so the hash only changes when the content or address does), and starts fcgiwrap. |
| `nginx.conf` | Serves the site on 80 and 443. It rewrites the Pages address to whatever address the reader used (`sub_filter`), serves only `ca.crt` out of `ssl/`, and serves the marketplace read-only over git smart HTTP. Claude Code makes a shallow clone, which plain static ("dumb") git hosting can't serve. |
| `docker-compose.release.yml`, `app.json`, `setup.py` | The sb90-deploy release description, the same shape as each app's. |

To try a build locally:

```bash
pip install "sb90-deploy[bundle]==0.6.0" --extra-index-url https://system-b90.github.io/.github/pypi/
python ops/mirror/build_site.py /tmp/mirror --tag v0.0.0
docker build -t sb90-mirror:dev /tmp/mirror
docker run --rm -p 8080:80 -e MIRROR_URL=http://localhost:8080 -v "$PWD/ssl:/etc/nginx/ssl:ro" sb90-mirror:dev
```

`ssl/` must hold `cert.pem` and `key.pem`. `python -c "from sb90_deploy.tls
import ensure_certificate as e; e('ssl', 'localhost')"` makes a pair.

## Not mirrored

- **npm packages** (`@system-b90/*` on GitHub Packages). They need a registry
  that speaks npm's API (e.g. Verdaccio), not static files.
- **The apps themselves.** Bluz, madash and peek-a-boo already ship their own
  offline bundles.
