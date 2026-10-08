# Private package index

A PEP 503 "simple" index for org packages that are not on PyPI
(`PyHiveLMS`, `bluz`).

## Quick Start

Consume it from a `requirements.txt`:

```
--extra-index-url https://system-b90.github.io/.github/pypi/

PyHiveLMS>=2.1.3
```

Or for a one-off install:

```bash
pip install --extra-index-url https://system-b90.github.io/.github/pypi/ PyHiveLMS
```

## Publishing a new version

```bash
cp dist/pyhivelms-<version>-py3-none-any.whl pypi/pyhivelms/
python pypi/generate_index.py pyhivelms   # omit the arg to regenerate everything
git add pypi && git commit -m "Vibe-Published pyhivelms <version>" && git push
```

Pages redeploys on push to `main`; the new version is installable once that
build finishes (usually under a minute).

## Serve it over Pages, not raw.githubusercontent.com

The index **must** be consumed at the `system-b90.github.io` URL. A
`raw.githubusercontent.com` URL cannot back a pip index at all:

- pip requests `<index>/<package>/` for a package. `raw` does not resolve a
  directory to its `index.html` — it returns 404. pip treats that as "package
  absent from this index" and silently falls back to PyPI, which for
  `PyHiveLMS` stops at 2.1.1. The failure surfaces much later as
  `No matching distribution found for PyHiveLMS>=2.1.3`.
- `--find-links` pointed straight at the `index.html` does not work either:
  `raw` serves it as `text/plain` with `X-Content-Type-Options: nosniff`, so
  pip refuses to parse links out of it.

Pages serves both the directory listings and `text/html`, which is what pip
needs.
