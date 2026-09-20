#!/usr/bin/env bash
# Waits for the Hive stack's Postgres container to be genuinely accepting TCP
# connections, rather than letting Compose's depends_on enforce it.
#
# Compose gives a dependency a fixed budget and then fails the whole bring-up
# with "dependency failed to start: container hive-postgres is unhealthy". On
# the shared self-hosted box that budget is not the binding constraint -- the
# host is. A run on 2026-07-24 spent 92s merely *creating* a container and 74s
# starting Postgres, leaving it ~34s to pass a healthcheck it would have passed
# shortly after. The database was fine; the host was busy.
#
# Waiting explicitly, with a budget scaled for a contended host, turns that into
# "slow but green" instead of a spurious failure, and prints the actual health
# status when it genuinely doesn't come up.
#
# Env:
#   DB_CID            container id of the `database` service (required)
#   DB_WAIT_ATTEMPTS  poll count, 5s apart (required)
set -uo pipefail

: "${DB_CID:?DB_CID is required}"
: "${DB_WAIT_ATTEMPTS:?DB_WAIT_ATTEMPTS is required}"

has_healthcheck=$(docker inspect --format '{{if .State.Health}}yes{{end}}' "$DB_CID" 2>/dev/null || true)
if [ "$has_healthcheck" != "yes" ]; then
  echo "The database container declares no healthcheck — skipping the explicit wait."
  exit 0
fi

echo "Waiting for Postgres to report healthy (up to $((DB_WAIT_ATTEMPTS * 5))s)..."
db_ok=""
stable=0
for i in $(seq 1 "$DB_WAIT_ATTEMPTS"); do
  status=$(docker inspect --format '{{.State.Health.Status}}' "$DB_CID" 2>/dev/null || echo unknown)
  # The container healthcheck is a bare `pg_isready`, which talks to the local
  # socket — and on a first boot the entrypoint runs initdb against a
  # *temporary* socket-only server before shutting it down and starting the
  # real one. That temp server answers the probe, so "healthy" here can be a
  # database that is about to disappear: the wait passed at 10s, and 35s later
  # compose's own depends_on re-check found it unhealthy and aborted the
  # bring-up.
  #
  # `-h 127.0.0.1` forces TCP, which the temp server does not listen on, so
  # only the real server can satisfy it. Requiring two consecutive passes also
  # rides out the shutdown between them.
  if [ "$status" = "healthy" ] && docker exec "$DB_CID" pg_isready -h 127.0.0.1 -p 5432 >/dev/null 2>&1; then
    stable=$((stable + 1))
    if [ "$stable" -ge 2 ]; then
      echo "Postgres healthy and accepting TCP after $((i * 5))s."
      db_ok=1
      break
    fi
    echo "Attempt $i/$DB_WAIT_ATTEMPTS — Postgres ready ($stable/2 consecutive), confirming..."
    sleep 5
    continue
  fi
  stable=0
  if [ "$status" = "unhealthy" ]; then
    # Keep waiting: on a loaded host Postgres often reports unhealthy for the
    # first probes and then recovers. Only the loop's overall budget decides
    # that it has genuinely failed.
    echo "Attempt $i/$DB_WAIT_ATTEMPTS — Postgres reports unhealthy, still waiting..."
  else
    echo "Attempt $i/$DB_WAIT_ATTEMPTS — Postgres status: $status"
  fi
  sleep 5
done

if [ -z "$db_ok" ]; then
  echo "::error::Postgres did not become healthy within $((DB_WAIT_ATTEMPTS * 5))s."
  docker inspect --format '{{json .State.Health}}' "$DB_CID" || true
  docker logs --tail 200 "$DB_CID" 2>&1 || true
  exit 1
fi
