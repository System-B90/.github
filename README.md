# System-B90 Shared CI

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
        uses: System-B90/.github/actions/setup-hive@main
        with:
          hive-token: ${{ secrets.CLASSIC_ACCESS_TOKEN || secrets.HIVE_REPO_TOKEN }}
          extra-hosts: 127.0.0.3 myapp.dev

      - name: Set up Node + Playwright
        uses: System-B90/.github/actions/setup-playwright@main

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
   pulls the images published by System-B90/pyhive's "Publish Hive Images"
   workflow (see below).
6. **Boot + init** — compose up, migrate, collectstatic, seed service
   accounts/tags/programs, non-interactive superuser (`admin`/`Password1`).
7. **Readiness check** — polls `https://hive.org/` until it responds.

Key inputs (all optional except `hive-token`): `hive-repo`, `hive-ref`,
`extra-hosts`, `python-version`, `image-source`, `registry-prefix`,
`registry-token`, `registry-tag`, `cache-version`, `free-disk-space`,
`wait-attempts`. Outputs: `hive-sha`, `cache-hit`.

### `actions/setup-playwright`

Node.js setup (with npm cache) + `npm ci` + Playwright browser install.
Inputs: `node-version` (default `24`), `install-command` (default `npm ci`),
`browsers` (default `chromium`).

## Build Hive once, reuse everywhere

By default every consumer repo builds Hive from source (mitigated by a
per-repo image cache — `actions/cache` does not share across repos). The end
state is that Hive is built **once** when its branch updates and every
consumer pulls the published images.

### The publisher: System-B90/pyhive "Publish Hive Images"

Since we don't control the Hive repo, publishing lives in
[System-B90/pyhive](https://github.com/System-B90/pyhive) (the org's
Hive-adjacent repo, which already holds a Hive PAT for its sync workflow).
Nightly (and on `workflow_dispatch`) it:

1. Resolves the tip of `hivelms/Hive@feature/sso`; exits early if
   `ghcr.io/system-b90/hive/core:<sha>` already exists.
2. Otherwise builds the prod images exactly as `setup-hive` does
   (`manage_hive.py build_deps` + `docker compose -f docker-compose.yaml build`).
3. Pushes every runtime image `hive/<service>` (base images excluded) as
   `ghcr.io/system-b90/hive/<service>:<commit-sha>` plus a `feature-sso`
   branch tag. The `core` anchor image is pushed last, so the existence
   check never sees a partial set.

**Package access:** the images contain the private Hive backend — packages
must stay **private**. Grant each consumer repo read access under the
package's settings → Manage Actions access; the consumer's default
`GITHUB_TOKEN` (the `registry-token` default) then works. Alternatively pass
a PAT with `read:packages` as `registry-token`.

### Switching a consumer to pulled images

One input:

```yaml
      - name: Set up Hive
        uses: System-B90/.github/actions/setup-hive@main
        with:
          hive-token: ${{ secrets.CLASSIC_ACCESS_TOKEN || secrets.HIVE_REPO_TOKEN }}
          image-source: registry
```

No other consumer changes are needed — the checkout (still required for the
compose file and init scripts), boot, and readiness steps are identical.

### If the Hive team ever publishes natively

A workflow in `hivelms/Hive` pushing the same
`<registry-prefix>/<service>:<sha>` layout on every push to the consumed
branch (instead of pyhive's nightly poll) makes publishing immediate —
consumers then just point `registry-prefix` at it. A `repository_dispatch`
to pyhive's publish workflow (like the `hive-release` dispatch it already
sends) achieves the same without moving the build.

## Versioning

Consumers reference `@main`. If a breaking change to an action is ever
needed, tag a release (`v1`, `v2`, …) and move consumers to tags.
