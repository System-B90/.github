# System-B15 Shared CI

Reusable composite actions for the org's CI pipelines. Consumer repos (Bluz,
Peek-a-boo, Madash) all run their E2E suites against a live Hive backend —
these actions keep that boot sequence in exactly one place instead of
copy-pasted workflow YAML.

## Quick Start

In a consumer repo's E2E workflow:

```yaml
jobs:
  e2e:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@v7

      - name: Set up Hive
        uses: System-B15/.github/actions/setup-hive@main
        with:
          hive-token: ${{ secrets.CLASSIC_ACCESS_TOKEN || secrets.HIVE_REPO_TOKEN }}
          extra-hosts: 127.0.0.3 myapp.dev

      - name: Set up Node + Playwright
        uses: System-B15/.github/actions/setup-playwright@main

      # ... boot your own stack, run tests ...
```

## Actions

### `actions/setup-hive`

Boots a full Hive stack (SSO identity provider + organizational data) on the
current runner and waits until it serves traffic. A composite action — not a
reusable workflow — because Hive must run on the **same runner** as the
consumer stack and the Playwright tests that hit it.

What it does, in order:

1. **Disk cleanup** — removes ~30 GB of preinstalled runner toolchains
   (.NET/Android/GHC/CodeQL) so the Hive images fit (`free-disk-space` input).
2. **Token verification** — fails early with actionable errors if the Hive
   PAT is missing/expired/unauthorized or the branch doesn't exist.
3. **Hive checkout** — blob-filtered clone of the private Hive repo.
4. **Hostname mapping** — `hive.org` → 127.0.0.1, plus consumer hosts via
   `extra-hosts`.
5. **Image acquisition** — `image-source: build` (default) builds from source
   with the built images cached per Hive commit SHA; `image-source: registry`
   pulls prebuilt images (see contract below).
6. **Boot + init** — compose up, migrate, collectstatic, seed service
   accounts/tags/programs, non-interactive superuser (`admin`/`Password1`).
7. **Readiness check** — polls `https://hive.org/` until it responds.

Key inputs (all optional except `hive-token`): `hive-repo`, `hive-ref`,
`extra-hosts`, `python-version`, `image-source`, `registry-prefix`,
`registry-tag`, `cache-version`, `free-disk-space`, `wait-attempts`.
Outputs: `hive-sha`, `cache-hit`.

### `actions/setup-playwright`

Node.js setup (with npm cache) + `npm ci` + Playwright browser install.
Inputs: `node-version` (default `24`), `install-command` (default `npm ci`),
`browsers` (default `chromium`).

## Roadmap: build Hive once, reuse everywhere

Today every consumer repo builds Hive from source (mitigated by a per-repo
image cache — `actions/cache` does not share across repos). The end state is
that Hive is built **once** when its branch updates and every consumer pulls
the published images.

### What the Hive team needs to add (publish contract)

A workflow in the Hive repo that, on every push to the consumed branch
(currently `feature/sso`):

1. Builds the prod images exactly as `setup-hive` does today
   (`manage_hive.py build_deps` + `docker compose -f docker-compose.yaml build`).
2. For every runtime image `hive/<service>:<tag>` (base images excluded),
   pushes it to a registry as:
   - `<registry-prefix>/<service>:<commit-sha>` (required — consumers pin by SHA)
   - `<registry-prefix>/<service>:<branch-tag>` (optional convenience tag)

   where `<registry-prefix>` defaults to `ghcr.io/hivelms/hive` in
   `setup-hive`, and `<service>` is the compose image name with the `hive/`
   prefix stripped.
3. Grants the consumer repos (or the org) read access to the packages.

Once that exists, consumers switch by adding one input:

```yaml
      - name: Set up Hive
        uses: System-B15/.github/actions/setup-hive@main
        with:
          hive-token: ${{ secrets.CLASSIC_ACCESS_TOKEN || secrets.HIVE_REPO_TOKEN }}
          image-source: registry
```

No other consumer changes are needed — the checkout (still required for the
compose file and init scripts), boot, and readiness steps are identical.

## Versioning

Consumers reference `@main`. If a breaking change to an action is ever
needed, tag a release (`v1`, `v2`, …) and move consumers to tags.
