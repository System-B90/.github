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
| **devops-py** | Shared dev-ops helpers behind each repo's `tools.py` — `sb90-devops`, published to the org pip index. Extracted from Bluz/madash copies (Bluz#226). |
| **deploy-py** | Shared deployment flows behind every app's release bundle — `sb90-deploy`, published to the org pip index. Release bundling (`actions/craft-release`), the bundle bootstrap (host Python 3.6+ → 3.10+ `.venv`), install, in-place upgrade, `link-hive`, and the `setup.py` wizard toolkit (TLS, Hive SSO via pyhive). Each app keeps only `deploy/app.json` + its own `setup.py`. Ported from Bluz's scripts. |
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
- `sb90-devops` (from `devops-py`), `sb90-deploy` (from `deploy-py`) and `bluz-cli` (from the private `bluz` repo) follow the identical pattern: `pip install bluz-cli --index-url https://system-b90.github.io/.github/pypi/`. `bluz`'s `release-pipeline.yml` `publish-cli-index` job copies each tagged release's wheel into `pypi/bluz-cli/` and regenerates the index on every `v*` tag push, using `CLASSIC_ACCESS_TOKEN` (bluz has no `ACCESS_TOKEN` secret — see Secrets available in CI below).
- App repos (`bluz`, `madash`, `peek-a-boo`) are unscoped, private, and don't publish — no `@system-b90/` prefix on their own `package.json` name.

## Claude Code plugins hosted here

Plugins live under `plugins/<name>/` — each is a self-contained Claude Code
plugin (`.claude-plugin/plugin.json` + `skills/`, optionally `hooks/`). The
marketplace itself is a single root-level `.claude-plugin/marketplace.json`
(name: `system-b90-marketplace`) listing every plugin by its `plugins/<name>`
path — plugin directories do **not** carry their own marketplace file.
`.github` is the distribution point for any plugin whose source repo is
private, so installing never requires cloning that private repo.

Currently hosted:

| Plugin | Source repo | What it does |
| --- | --- | --- |
| `bluz-cli` | `bluz` (private) | Skill + auto-install for the `bluz` CLI. `SessionStart` hook `pip install`s `bluz-cli` from this repo's pip index (see Package conventions) if missing — no Bluz checkout needed. |

Install any hosted plugin:

```
/plugin marketplace add System-B90/.github
/reload-plugins
/plugin install <plugin-name>@system-b90-marketplace
/reload-plugins
```

e.g. `/plugin install bluz-cli@system-b90-marketplace`.

Adding a new plugin here: create `plugins/<name>/` following the `bluz-cli`
layout, then add an entry to the root `.claude-plugin/marketplace.json` with
`"source": "./plugins/<name>"` and a row to the table above.

## Git workflow

- Never commit directly to `main`/`master` — always use a feature branch.
- For parallel work, use git worktrees: `git worktree add ../repo-wt-<feature> -b <branch>`. Clean up worktrees after merging.
- **Commit message format: `Vibe-<PastTenseVerb> <description>`** — e.g. `Vibe-Implemented`, `Vibe-Fixed`, `Vibe-Refactored`, `Vibe-Removed`. No `feat:`/`fix:`/`chore:` prefixes anywhere in the org.
- PR target branch: `master` everywhere. This previously said bluz targets a `dev` branch; bluz has no `dev` branch (verified 2026-08-03 — its long-lived branch is `master`), so that instruction sent PRs at a base that does not exist.
- **Never skip commit hooks** (no `-n` / `--no-verify`) — run the repo's auto-fixers first (see CI/CD rules below) so the Husky pre-commit hook passes cleanly instead of being bypassed.
  - **Known conflict:** `bluz`'s own `CLAUDE.md` tells agents to auto-commit with `-n`. That contradicts this rule and this rule wins — flagged here rather than silently overridden. Fix belongs in `bluz/CLAUDE.md`.

## CI/CD rules

- Run auto-fixers before committing — never paper over lint failures with `eslint-disable` comments:
  - JS/TS: `npx eslint --fix && npx prettier --write`
  - Python: `ruff format . && ruff check --fix .`
- For failing tests that are genuine bugs (not something you can fix in scope): use `test.fails()` or `test.skip()` and open a GitHub issue. **Never delete tests.**
- **Regression tests for bugs:** Every closed bug issue must have a dedicated regression test committed alongside the fix. The test must fail on the pre-fix code and pass after. This prevents bugs from silently resurfacing.
- Never push to archived repos.
- Never skip hooks (`--no-verify`, `-n`) to force a commit through.

## Runners

**Long-running work belongs on the self-hosted runner
(`runs-on: self-hosted`).** GitHub-hosted minutes are scarce, so anything that
boots a Hive stack, builds images, or runs an E2E suite must target
self-hosted.

**Small, infrequent jobs may use GitHub-hosted runners.** A lint-and-unit-test
job that finishes in under a minute and only fires on pull requests to one
package is not what the minutes budget is about, and hosted runners buy things
the pool cannot give you — most concretely `windows-latest`, since the pool is
Linux-only. `devops-py`'s CI is the worked example: every helper in it branches
on `sys.platform` and the win32 branches are the ones that actually break, so a
real Windows leg is worth more than the ~45s of hosted time it costs.

Judge by cost and frequency, not by rule. If a job is minutes long, runs on
every push, or fans out into a matrix of heavy legs, it goes self-hosted.

The runner is **not** a single serialized agent. It's an autoscaled pool of
ephemeral docker-in-docker runners (label `dind`; `mks-srvu-dind-<random>`, one per job, each
with its own Docker daemon) sharing one 8-vCPU / 23 GB physical box. Observed
directly on 2026-07-24: runner ids 141 and 143 executing two pyhive jobs while
peek-a-boo's E2E ran alongside them.

That combination — real concurrency, one physical box — is the thing to design
around, and it bites in a specific way:

- **Total concurrent work is the scarce resource, not runner slots.** Jobs do
  run in parallel, so splitting a workflow into `lint` / `test` / `build`
  doesn't queue them behind each other. It does make each one pay for its own
  checkout and `npm ci`, and it puts all of that on the box at once. Prefer one
  job with sequential steps anyway — not because the split serializes, but
  because it multiplies total I/O on a box that is already the bottleneck.
  Reserve separate jobs for genuine fan-out or `needs:` gating.
- **Contention shows up as timeouts, not as queueing.** Under load this box has
  taken **92 seconds to create a single container** and 23 minutes on a "Set up
  runner" step. Anything with a healthcheck or a fixed wait can fail purely
  because the host is busy — see the Hive/Postgres case in
  `actions/setup-hive`, which now waits on the database's health itself rather
  than relying on Compose's dependency timeout.
- **Always set `timeout-minutes`.** Not because a hung job blocks the queue,
  but because a wedged job holds a slice of a shared box indefinitely.
- **Docker state across jobs is inconsistent — assume nothing, clean up
  defensively.** Two runs on 2026-07-24 behaved differently. Both re-pulled
  every Hive image from the registry ("Downloaded newer image"), so there is no
  warm image cache to rely on. But hive-core's run found eight Hive containers
  already `Running` at its first `docker compose up -d`, left over from an
  earlier run, and Compose had to `Recreate` the rest — one of which
  (`hive-nginx`) took **11.5 minutes**. So a job may or may not inherit a live
  stack. This is why `actions/setup-hive` tears leftovers down before booting
  rather than trusting the daemon to be clean: on the run that inherited a
  stack, that teardown is the difference between recreating containers under
  load and starting from nothing.
- **E2E stacks don't collide on ports, they collide on CPU and disk.** Each
  dind has its own network namespace, so two Hive stacks binding
  `0.0.0.0:80/443` coexist fine. What they can't do is boot at the same time on
  8 shared vCPUs without pushing each other past their healthchecks.

If E2E jobs across repos keep failing on healthchecks, the lever is reducing
how many land at once (or giving the pool a bigger box) — not adding retries
downstream of the real constraint.

`actions/setup-hive` and `actions/setup-playwright` both branch on
`runner.environment`, so their GitHub-hosted-only behaviour (toolchain disk
purge, `playwright install --with-deps`) switches off automatically on
self-hosted. Override with their `free-disk-space` / `with-deps` inputs.

### Shared persistent Hive (`shared-hive` runners)

`mks90-laptop-wsl`, `-02` and `-03` (label `shared-hive`) run as the dedicated
`hive-ci` user (systemd services) on one WSL host and share its Docker daemon.
A persistent Hive lives there under `/home/hive-ci/hive-shared` (compose
project `hive`, network `hive_hive-net`, `https://hive.org`, `admin`/`api` with
password `Password1`). It is for **small, non-destructive** e2e verifications:

- `actions/shared-hive-acquire` — waits on a host `flock` (one job at a time
  across all three runners), resets Hive to its baseline, and cancels the run if
  it still holds the instance after `max-minutes` (default **25**). Needs
  `permissions: actions: write`. Do builds/installs *before* it.
- `actions/shared-hive-release` — `if: always()` last step: resets and unlocks.
- Reset = Postgres `CREATE DATABASE ... TEMPLATE hive_ci_baseline` + Redis
  flush (~20s). Media/course files are **not** reset.
- New Hive images / broken baseline: run acquire with `rebuild: true` and a
  `stack-token`, or on the host `hive-shared.sh bootstrap <hive-stack-dir>`.
  Root host setup is `actions/shared-hive/host-setup.sh`.
- These runners are **not** `dind`: `setup-hive` refuses to run there because
  its cleanup would delete the shared instance.

Bluz's `e2e.yml` keeps a `workflow_dispatch` escape hatch
(`target: github-hosted`) that runs the classic 3-shard matrix. Use it only if
GitHub-hosted minutes come back and a run genuinely needs the parallelism.

## Secrets available in CI

Secret names are **not** uniform across repos — verify with `gh secret list` in the target repo before assuming a name exists; don't copy a workflow's `secrets.X` reference across repos without checking.

- `SYSTEM_B90_READ` — the only PAT confirmed present in every repo (as of 2026-07-19). Read-scoped; not sufficient for pushes to other repos.
- `ACCESS_TOKEN` — PAT with repo + packages scope, used for cross-repo operations (e.g. pyhive's `publish.yml` pushing into `.github`). Present in `madash`, `peek-a-boo`, `pyhive`; **absent** from `bluz`, `hive-core`, `session-ws`, `hive-nextauth`.
- `CLASSIC_ACCESS_TOKEN` — used as an `ACCESS_TOKEN` fallback in some workflows (e.g. `bluz`, pyhive's `publish-hive-images.yml`); present in `bluz` and `devops-py`, where `ACCESS_TOKEN` is not. Both use it to push built wheels into this repo's `pypi/` index.
- `HIVE_REPO_TOKEN` — scoped for checking out/pushing to Hive-related repos; present in `bluz`, `pyhive`.
- `GITHUB_TOKEN` — standard Actions token, auto-provided, limited to the current repo.
- `CI_LOCK_TOKEN` — **does not exist yet.** Needed by `actions/ci-lock` to serialise
  Hive-booting jobs across repos; must be a PAT with `contents:write` on `.github`,
  available to every repo that boots Hive. `SYSTEM_B90_READ` is read-only and will not
  work. Until it exists, `ci-lock`/`ci-unlock` warn and no-op, and E2E jobs across repos
  stay unserialised.

## What NOT to do

- Never touch `hivelms/Hive` (different org, completely off limits).
- Never commit directly to `main`/`master`.
- Never add `eslint-disable` comments to silence linting — fix the underlying issue.
- Never delete tests (skip or mark as expected-fail instead, with an issue filed).
- Never push to archived repos.
- Never skip commit hooks by default.
- Never change repo visibility or org access controls without explicit user instruction.
