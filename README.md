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
    # E2E boots a real Hive stack — long-running work goes self-hosted.
    # (Small, infrequent jobs may use hosted runners; see CLAUDE.md.)
    runs-on: self-hosted
    # Not for queueing (jobs run in parallel), but so a wedged job cannot hold
    # a slice of the shared box indefinitely.
    timeout-minutes: 60
    steps:
      - uses: actions/checkout@v7

      # Serialise against every other Hive stack in the org. Two booting at
      # once on the shared 8-vCPU box push each other past their healthchecks.
      - name: Take the E2E lock
        id: ci_lock
        uses: System-B90/.github/actions/ci-lock@main
        with:
          token: ${{ secrets.CI_LOCK_TOKEN }}

      - name: Set up Hive
        uses: System-B90/.github/actions/setup-hive@main
        with:
          hive-token: ${{ secrets.CLASSIC_ACCESS_TOKEN || secrets.HIVE_REPO_TOKEN }}
          extra-hosts: 127.0.0.3 myapp.dev

      - name: Set up Node + Playwright
        uses: System-B90/.github/actions/setup-playwright@main

      # ... boot your own stack, run tests ...

      # Both cleanup steps must run even when the tests fail, or the box keeps
      # filling up and the next repo waits out the lock's stale timeout.
      - name: Tear down Hive
        if: always()
        uses: System-B90/.github/actions/teardown-hive@main

      - name: Release the E2E lock
        if: always()
        uses: System-B90/.github/actions/ci-unlock@main
        with:
          token: ${{ secrets.CI_LOCK_TOKEN }}
          acquired: ${{ steps.ci_lock.outputs.acquired }}
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

Beyond the ordered steps above, `setup-hive` refuses to start when the runner
has less than `min-free-disk-gb` (default 10) free after cleanup. Every symptom
in [#12](https://github.com/System-B90/.github/issues/12) — `dockerd not ready
after 120s`, 92-second container creation, unhealthy Postgres — is what a full
host looks like from inside a job that already spent 20 minutes getting there.
Failing at the preflight costs seconds and names the actual cause.

### `actions/teardown-hive`

Brings the Hive stack down and reclaims its disk. Call it with `if: always()`
as the last step of any job that used `setup-hive`.

`setup-hive` already clears leftovers at the *start* of a run, which keeps that
run correct but leaves a dead stack occupying the box in between. Releasing at
the end shrinks that window to nothing. Never fails the job — a cleanup error
turning a green run red would be a worse bug than the one it fixes.

Inputs: `hive-path`, `prune` (`safe` | `aggressive` | `none`), `report-disk`.

### `actions/teardown-test-stack`

The app-side counterpart of `teardown-hive`. Removes every compose project
whose containers are named `<prefix>*` (containers, anonymous and named
volumes, networks), including a project whose compose file is gone. Run it
before a job to reclaim a stack a dead run leaked, and with `if: always()`
after it. Refuses a `hive` prefix and never fails the job.

```yaml
- uses: System-B90/.github/actions/teardown-test-stack@main
  with:
    prefix: bluz-test-
```

Inputs: `prefix` (required), `compose-files` (extra `-f` files for
`compose down`), `prune` (`"true"` also prunes all unused volumes, images and
build cache; throwaway VMs only, never on the shared-hive box).

### `actions/ci-lock` and `actions/ci-unlock`

A mutex **across repositories**. GitHub's `concurrency:` key only serialises
within one repo, and the contention that matters here is between them: bluz,
peek-a-boo, madash and hive-core each boot a Hive stack onto the same 8-vCPU
host, and two arriving together push both past their healthchecks.

The lock is a file created through the Contents API on a `ci-locks` branch of
this repo. Creating a file without passing its blob SHA fails when the path
exists — that rejection is the atomic test-and-set. The body records the holder
and a timestamp, so a lock orphaned by a cancelled run is reclaimed on age
(`stale-minutes`, default 75) instead of wedging every repo's E2E.

**Requires a `CI_LOCK_TOKEN` secret** — a PAT with `contents:write` on this
repo, available to every repo that boots Hive. `SYSTEM_B90_READ` is read-only
and will not work. Without the secret both actions warn and no-op, so a repo
that lacks it still runs; it just isn't serialised.

`ci-unlock` is a separate action because composite actions cannot register
post-job steps. Always call it with `if: always()`, passing `ci-lock`'s
`acquired` output — it deletes the lock only if this job still holds it, so a
lock already reclaimed as stale is left with its new owner.

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
