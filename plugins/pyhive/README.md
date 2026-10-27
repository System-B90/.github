# pyhive plugin

Claude Code plugin: teaches an agent to drive the `pyhive` CLI and the PyHive
Python SDK (Hive LMS), and installs PyHive if it is missing — **no pyhive
checkout required**.

## Quick Start

```
/plugin marketplace add System-B90/.github
/plugin install pyhive@system-b90-marketplace
```

(`system-b90-marketplace` is the marketplace name from the repo-root
`.claude-plugin/marketplace.json` — not the plugin name.)

On the next session start, the plugin checks that `pyhive docs path` works and
otherwise `pip install --upgrade`s `PyHiveLMS` from
`https://system-b90.github.io/.github/pypi/` (as an extra index — PyHive's
dependencies come from PyPI). No auth, no clone.

## What it does

- Ships the `pyhive` skill (`skills/pyhive/SKILL.md` plus the CLI, SDK and
  examples pages it links to).
- Runs a `SessionStart` hook (`hooks/ensure-pyhive.js`) that installs or
  upgrades PyHive when the CLI is missing or predates `pyhive docs`. Never
  blocks session start on error.

## Where the skill comes from

`skills/pyhive/` is **generated — do not edit it here**. It is a copy of
`pyhive/docs/*.md` in System-B90/pyhive, the same files that ship inside the
wheel (`pyhive docs show <page>`) and build the docs site at
`https://system-b90.github.io/.github/pyhive/`. pyhive's
`.github/workflows/docs.yml` refreshes both this directory and `pyhive/` at
the repo root on every `v*` tag. Fix the docs in pyhive instead.

Without this plugin, the same skill installs from the package itself:
`pyhive docs install-skill`.

## Uninstall

```
/plugin uninstall pyhive@system-b90-marketplace
```
