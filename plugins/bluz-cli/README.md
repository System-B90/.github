# bluz-cli plugin

Claude Code plugin: teaches an agent to drive the `bluz` CLI and auto-installs
it if missing — **no Bluz source checkout required**. `bluz` (Bluz's app repo)
is private; this plugin lives in the public `System-B90/.github` repo and
installs the CLI from the org's public pip index instead.

## Quick Start

```
/plugin marketplace add System-B90/.github
/plugin install bluz-cli@bluz-cli
```

On the next session start, the plugin checks whether `bluz` is on PATH and
installs it from `https://system-b90.github.io/.github/pypi/`
if it isn't — no auth, no Bluz clone.

## What it does

- Ships the `bluz-cli` skill (`skills/bluz-cli/SKILL.md`) — command reference,
  payload shapes, output parsing conventions, known server bugs.
- Runs a `SessionStart` hook (`hooks/ensure-bluz-cli.js`) that silently
  `pip install`s `bluz-cli` from the org pip index if `bluz --version` fails.
  Never blocks session start on error.

## How the CLI gets published here

Bluz's `.github/workflows/release-pipeline.yml` `publish-cli-index` job runs
on every `v*` tag: builds `cli/dist/*`, copies it into this repo's
`pypi/bluz-cli/`, regenerates the PEP 503 index via `pypi/generate_index.py`,
and pushes. Same mechanism pyhive uses for `pyhivelms`.

## Uninstall

```
/plugin uninstall bluz-cli@bluz-cli
```
