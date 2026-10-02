# System-B90

מערכות בלמ"סיות עבור הבי"ס — LMS tooling for a school, built around the
[Hive](https://github.com/HiveLMS) backend.

Most repos here are private. This page is the public entry point: what each
one is, and how to get it running.

---

## Quick start

### Install a CLI

`bluz-cli` drives the Bluz scheduling and curriculum API from a terminal. No
checkout needed:

```bash
pip install bluz-cli --index-url https://system-b90.github.io/.github/pypi/
bluz login
```

`PyHiveLMS`, the Python client for the Hive API, installs the same way:

```bash
pip install PyHiveLMS --index-url https://system-b90.github.io/.github/pypi/
```

Both come from the org's own PEP 503 index, hosted in this repo and served
over GitHub Pages. It needs no authentication.

### Use a shared npm package

The `@system-b90/*` packages publish to GitHub Packages (`command-palette` is the exception: it is on the official npm registry, so a plain `npm install @system-b90/command-palette` works). Point the scope at
that registry once:

```bash
echo "@system-b90:registry=https://npm.pkg.github.com" >> .npmrc
npm install @system-b90/hive-core
```

Installing needs a `GITHUB_TOKEN` or `NPM_TOKEN` carrying `read:packages`.

### Run an app locally

Every app repo ships a `tools.py` dev-ops CLI. From a fresh clone:

```bash
python scripts/setup.py    # interactive: writes .env, SSL certs, registers SSO
python tools.py dev        # backgrounds the dev servers, returns immediately
python tools.py dev status # what is actually up
```

`python tools.py ci` runs the same pipeline CI does — lint, unit tests, and
the E2E suite against a real Hive stack.

### Install the Claude Code plugin

```
/plugin marketplace add System-B90/.github
/plugin install bluz-cli@system-b90-marketplace
```

Its `SessionStart` hook installs `bluz-cli` from the index above if it is
missing, so no Bluz checkout is required.

---

## The repos

**Applications**

| Repo | What it is |
| --- | --- |
| [Bluz](https://github.com/System-B90/Bluz) | The primary product — scheduling and curriculum (Gantt) management. Ships the `bluz-cli` companion CLI. |
| [madash](https://github.com/System-B90/madash) | Status dashboard — journal, board, system health. |
| [peek-a-boo](https://github.com/System-B90/peek-a-boo) | Student monitoring. |

**Libraries**

| Repo | Package |
| --- | --- |
| [pyhive](https://github.com/System-B90/pyhive) | `PyHiveLMS` — Python client for the Hive API. |
| [hive-core](https://github.com/System-B90/hive-core) | `@system-b90/hive-core` — shared types and error classes. |
| [hive-nextauth](https://github.com/System-B90/hive-nextauth) | `@system-b90/hive-nextauth` — NextAuth.js + Hive SSO helpers. |
| [session-ws](https://github.com/System-B90/session-ws) | `@system-b90/session-ws` — shared WebSocket session server. |
| [command-palette](https://github.com/System-B90/command-palette) | `@system-b90/command-palette` — VSCode-style command palette for MUI apps. Public. |
| [devops-py](https://github.com/System-B90/devops-py) | `sb90-devops` — shared dev-ops helpers behind each repo's `tools.py`. |

**Infrastructure**

| Repo | What it is |
| --- | --- |
| [.github](https://github.com/System-B90/.github) | This repo — reusable CI workflows, composite actions, the pip index, the docs site, and Claude Code plugins. |
| [bin](https://github.com/System-B90/bin) | Installation system for programs and configurations. |

---

## Documentation

The docs site is served from this repo over GitHub Pages:
**<https://system-b90.github.io/.github/bluz/>**

Per-repo contributor docs — architecture, stack, conventions, testing — live
in each repo's `CONTRIBUTING.md` and `CLAUDE.md`.

## Getting help

Open an issue in the repo the problem belongs to. Cross-cutting or org-level
questions go in [.github](https://github.com/System-B90/.github/issues).
