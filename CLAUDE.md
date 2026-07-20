# CLAUDE.md — System-B90 org

Guidance for Claude Code / agentic sessions working anywhere in the System-B90 org. Repo-specific `CLAUDE.md` files (bluz, madash, peek-a-boo, pyhive) extend this; when they conflict on something org-wide, treat that as a bug to flag, not a silent override.

## Org overview

- **System-B90** — מערכות בלמ"סיות עבור הבי"ס — LMS tooling for a school.
- Org: `github.com/System-B90`. All repos are **private**, except `.github` itself — GitHub requires the org-profile `.github` repo to be public for its README/health files to render.
- This file lives in the `.github` repo (checked out locally as `org-github` — the directory name doesn't match the GitHub repo name, don't let that confuse path assumptions).

## Repos and their purpose

| Repo | Purpose |
| --- | --- |
| **bluz** | Main frontend/backend app. Scheduling + curriculum (Gantt) management. Next.js 14, TypeScript. The primary product. Ships a companion `bluz-cli` Python CLI, published to the org's pip index (see Package conventions) — its Claude Code plugin lives here in `.github` under `plugins/bluz-cli/` since bluz itself is private. |
| **madash** | Secondary app — status/dashboard (journal, call-to-Hadas board, system health). Next.js, TypeScript. Stateless, no DB. |
| **peek-a-boo** | Third app — student monitoring. Next.js, TypeScript. |
| **pyhive** | Python client library for the Hive LMS API. Install via the org's pip index (see Package conventions below), or `pip install git+https://github.com/System-B90/pyhive.git@master` for an unreleased ref. |
| **hive-core** | Shared TypeScript types and error classes — `@system-b90/hive-core`. |
| **session-ws** | Shared WebSocket session server — `@system-b90/session-ws`. |
| **hive-nextauth** | Shared NextAuth.js + Hive SSO helpers — `@system-b90/hive-nextauth`. |
| **.github** | Org-wide CI reusable workflows and composite actions (this repo). |

Local checkouts all live under `C:\Users\mkupe\Code\system-b90\<repo-name>`. Directories suffixed `-wt-*` (e.g. `bluz-wt-shared-pkgs`) are `git worktree` checkouts of the main repo on a different branch, not independent repos.

## The Hive backend

- Hive is a Django/Python LMS backend maintained by the **HiveLMS** org — a different org, not System-B90.
- **Never touch `hivelms/Hive` or anything under the hivelms org.** It is completely off limits.
- Integrate with Hive only via its API. Never modify Hive source.
- The Hive OpenAPI spec lives at `api/core.yaml` in the pyhive repo (`C:\Users\mkupe\Code\system-b90\pyhive`) and is what pyhive's typed core is generated from.

## Tech stack

- **Frontend/backend**: Next.js (App Router), TypeScript, React.
- **Styling**: Tailwind CSS (+ MUI in bluz/madash/peek-a-boo).
- **Auth**: NextAuth.js with Hive SSO (JWT).
- **WebSockets**: `@system-b90/session-ws`.
- **Testing**: Vitest (unit), Playwright (e2e).
- **Linting**: ESLint + Prettier (JS/TS), Ruff (Python).
- **CI**: GitHub Actions, using this repo's reusable workflows/composite actions where possible.
- **Docker**: Docker Compose for local dev and e2e test environments (Hive + app).

## Package conventions

- All shared npm packages are scoped `@system-b90/*`, published to GitHub Packages.
- To install: add an `.npmrc` with `@system-b90:registry=https://npm.pkg.github.com`.
- Auth requires `NPM_TOKEN` or `GITHUB_TOKEN` with `read:packages` scope.
- pyhive is **not** on the official PyPI. It's published to a PEP 503 index hosted as static files in this repo (`pypi/`), served over **GitHub Pages** (`https://system-b90.github.io/.github/`). No auth is required to install — `.github` is public (see Org overview above):
  `pip install PyHiveLMS --index-url https://system-b90.github.io/.github/pypi/`
  `pyhive`'s `publish.yml` copies each tagged release's wheels into `pypi/pyhivelms/` (the PEP 503-normalized project name — **not** `pyhive`, the import name) and regenerates `pypi/generate_index.py`'s output here on every `v*` tag push. For an unreleased ref, `git+https://...` still works (that one does need SSH/HTTPS git creds, since `pyhive` itself is private).
  GitHub Pages is CDN-cached (roughly a few minutes TTL) — a just-published release may not show up in the index immediately.
  **Note:** `raw.githubusercontent.com` does NOT work for this — it maps URLs 1:1 to repo file paths with no directory-index fallback, so pip's request for the bare package directory (`pypi/<pkg>/`) 404s even though `generate_index.py` writes a valid `index.html` there. GitHub Pages serves that `index.html` for directory requests, which is why the index has to be hosted there instead.
- `bluz-cli` (from the private `bluz` repo) follows the identical pattern: `pip install bluz-cli --index-url https://system-b90.github.io/.github/pypi/`. `bluz`'s `release-pipeline.yml` `publish-cli-index` job copies each tagged release's wheel into `pypi/bluz-cli/` and regenerates the index on every `v*` tag push, using `CLASSIC_ACCESS_TOKEN` (bluz has no `ACCESS_TOKEN` secret — see Secrets available in CI below).
- App repos (`bluz`, `madash`, `peek-a-boo`) are unscoped, private, and don't publish — no `@system-b90/` prefix on their own `package.json` name.

## Claude Code plugins hosted here

Plugins live under `plugins/<name>/` — each is a self-contained Claude Code
plugin (`.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` +
`skills/`, optionally `hooks/`). `.github` is the distribution point for any
plugin whose source repo is private, so installing never requires cloning
that private repo.

Currently hosted:

| Plugin | Source repo | What it does |
| --- | --- | --- |
| `bluz-cli` | `bluz` (private) | Skill + auto-install for the `bluz` CLI. `SessionStart` hook `pip install`s `bluz-cli` from this repo's pip index (see Package conventions) if missing — no Bluz checkout needed. |

Install any hosted plugin:

```
/plugin marketplace add System-B90/.github
/plugin install <plugin-name>@<plugin-name>
```

e.g. `/plugin install bluz-cli@bluz-cli`.

Adding a new plugin here: create `plugins/<name>/` following the `bluz-cli`
layout, keep its `marketplace.json` `source` as `"./"` (self-referencing,
consistent with `bluz-cli`'s), and add a row to the table above.

## Git workflow

- Never commit directly to `main`/`master` — always use a feature branch.
- For parallel work, use git worktrees: `git worktree add ../repo-wt-<feature> -b <branch>`. Clean up worktrees after merging.
- **Commit message format: `Vibe-<PastTenseVerb> <description>`** — e.g. `Vibe-Implemented`, `Vibe-Fixed`, `Vibe-Refactored`, `Vibe-Removed`. No `feat:`/`fix:`/`chore:` prefixes anywhere in the org.
- PR target branch: `master` for most repos; `dev` for bluz feature work specifically (bluz has a live `dev` branch that other repos don't).
- **Never skip commit hooks** (no `-n` / `--no-verify`) — run the repo's auto-fixers first (see CI/CD rules below) so the Husky pre-commit hook passes cleanly instead of being bypassed.

## CI/CD rules

- Run auto-fixers before committing — never paper over lint failures with `eslint-disable` comments:
  - JS/TS: `npx eslint --fix && npx prettier --write`
  - Python: `ruff format . && ruff check --fix .`
- For failing tests that are genuine bugs (not something you can fix in scope): use `test.fails()` or `test.skip()` and open a GitHub issue. **Never delete tests.**
- **Regression tests for bugs:** Every closed bug issue must have a dedicated regression test committed alongside the fix. The test must fail on the pre-fix code and pass after. This prevents bugs from silently resurfacing.
- Never push to archived repos.
- Never skip hooks (`--no-verify`, `-n`) to force a commit through.

## Secrets available in CI

Secret names are **not** uniform across repos — verify with `gh secret list` in the target repo before assuming a name exists; don't copy a workflow's `secrets.X` reference across repos without checking.

- `SYSTEM_B90_READ` — the only PAT confirmed present in every repo (as of 2026-07-19). Read-scoped; not sufficient for pushes to other repos.
- `ACCESS_TOKEN` — PAT with repo + packages scope, used for cross-repo operations (e.g. pyhive's `publish.yml` pushing into `.github`). Present in `madash`, `peek-a-boo`, `pyhive`; **absent** from `bluz`, `hive-core`, `session-ws`, `hive-nextauth`.
- `CLASSIC_ACCESS_TOKEN` — used as an `ACCESS_TOKEN` fallback in some workflows (e.g. `bluz`, pyhive's `publish-hive-images.yml`); present in `bluz` where `ACCESS_TOKEN` is not.
- `HIVE_REPO_TOKEN` — scoped for checking out/pushing to Hive-related repos; present in `bluz`, `pyhive`.
- `GITHUB_TOKEN` — standard Actions token, auto-provided, limited to the current repo.

## What NOT to do

- Never touch `hivelms/Hive` (different org, completely off limits).
- Never commit directly to `main`/`master`.
- Never add `eslint-disable` comments to silence linting — fix the underlying issue.
- Never delete tests (skip or mark as expected-fail instead, with an issue filed).
- Never push to archived repos.
- Never skip commit hooks by default.
- Never change repo visibility or org access controls without explicit user instruction.
