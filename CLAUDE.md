# CLAUDE.md — System-B90 org

Guidance for Claude Code / agentic sessions working anywhere in the System-B90 org. Repo-specific `CLAUDE.md` files (bluz, madash, peek-a-boo, pyhive) extend this; when they conflict on something org-wide, treat that as a bug to flag, not a silent override.

## Org overview

- **System-B90** — מערכות בלמ"סיות עבור הבי"ס — LMS tooling for a school.
- Org: `github.com/System-B90`. All repos are **private**.
- This file lives in the `.github` repo (checked out locally as `org-github` — the directory name doesn't match the GitHub repo name, don't let that confuse path assumptions).

## Repos and their purpose

| Repo | Purpose |
| --- | --- |
| **bluz** | Main frontend/backend app. Scheduling + curriculum (Gantt) management. Next.js 14, TypeScript. The primary product. |
| **madash** | Secondary app — status/dashboard (journal, call-to-Hadas board, system health). Next.js, TypeScript. Stateless, no DB. |
| **peek-a-boo** | Third app — student monitoring. Next.js, TypeScript. |
| **pyhive** | Python client library for the Hive LMS API. Install: `pip install git+https://github.com/System-B90/pyhive.git@main`. |
| **hive-core** | Shared TypeScript types and error classes — `@system-b90/hive-core`. |
| **session-ws** | Shared WebSocket session server — `@system-b90/session-ws`. |
| **hive-nextauth** | Shared NextAuth.js + Hive SSO helpers — `@system-b90/hive-nextauth`. |
| **.github** | Org-wide CI reusable workflows and composite actions (this repo). |

Local checkouts all live under `C:\Users\mkupe\Code\system-b15\<repo-name>` — the parent directory is still named `system-b15` even though the org itself is `System-B90`. Directories suffixed `-wt-*` (e.g. `bluz-wt-shared-pkgs`) are `git worktree` checkouts of the main repo on a different branch, not independent repos.

## The Hive backend

- Hive is a Django/Python LMS backend maintained by the **HiveLMS** org — a different org, not System-B90.
- **Never touch `hivelms/Hive` or anything under the hivelms org.** It is completely off limits.
- Integrate with Hive only via its API. Never modify Hive source.
- The Hive OpenAPI spec lives at `api/core.yaml` in the pyhive repo (`C:\Users\mkupe\Code\system-b15\pyhive`) and is what pyhive's typed core is generated from.

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
- pyhive installs via `git+https://...`, **not** PyPI.
- App repos (`bluz`, `madash`, `peek-a-boo`) are unscoped, private, and don't publish — no `@system-b90/` prefix on their own `package.json` name.

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

- `ACCESS_TOKEN` — PAT with repo + packages scope, available in all repos, used for cross-repo operations.
- `NPM_TOKEN` — alias for `ACCESS_TOKEN`, used for GitHub Packages auth.
- `GITHUB_TOKEN` — standard Actions token, limited to the current repo.

## What NOT to do

- Never touch `hivelms/Hive` (different org, completely off limits).
- Never commit directly to `main`/`master`.
- Never add `eslint-disable` comments to silence linting — fix the underlying issue.
- Never delete tests (skip or mark as expected-fail instead, with an issue filed).
- Never push to archived repos.
- Never skip commit hooks by default.
- Never change repo visibility or org access controls without explicit user instruction.
