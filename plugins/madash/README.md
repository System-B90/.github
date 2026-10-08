# madash plugin

Claude Code plugin: teaches an agent to drive the `madash` CLI and auto-installs
it if missing — **no source checkout required**. The app repo may be private;
this plugin lives in the public `System-B90/.github` repo and
installs the CLI from the org's public pip index instead.

## Quick Start

```
/plugin marketplace add System-B90/.github
/plugin install madash@system-b90-marketplace
```

(`system-b90-marketplace` is the marketplace name from the repo-root
`.claude-plugin/marketplace.json` — not the plugin name.)

On the next session start, the plugin checks whether `madash` is on PATH and
installs it from `https://system-b90.github.io/.github/pypi/` (as an extra
index — the CLI's dependencies come from PyPI)
if it isn't — no auth, no clone.

## What it does

- Ships the `madash` skill (`skills/madash/SKILL.md`) — command reference,
  payload shapes, output parsing conventions, known server bugs.
- Runs a `SessionStart` hook (`hooks/ensure-madash.js`) that silently
  `pip install`s `madash` from the org pip index if `madash --version` fails.
  Never blocks session start on error.

## How the CLI gets published here

madash's `.github/workflows/release.yml` `publish-cli-index` job runs
on every `v*` tag: builds `cli/dist/*`, copies it into this repo's
`pypi/madash/`, regenerates the PEP 503 index via `pypi/generate_index.py`,
and pushes. Same mechanism pyhive uses for `pyhivelms`. The package appears in the index from
the app's first release tag after the CLI landed.

## Uninstall

```
/plugin uninstall madash@system-b90-marketplace
```
