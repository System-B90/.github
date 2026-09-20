#!/usr/bin/env bash
# Brings the Hive stack down and removes whatever Compose no longer knows
# about. Best-effort throughout: a cleanup error must never turn a green run
# red, so this always exits 0.
#
# Env:
#   HIVE_PATH   directory Hive was checked out into (required)
set -u

: "${HIVE_PATH:?HIVE_PATH is required}"

if [ -f "${HIVE_PATH}/docker-compose.yaml" ]; then
  echo "Bringing the Hive stack down..."
  docker compose -f "${HIVE_PATH}/docker-compose.yaml" down -v --remove-orphans
else
  echo "No ${HIVE_PATH}/docker-compose.yaml — nothing to compose-down."
fi

# Compose only removes what its project file still describes. A stack that was
# killed mid-bring-up, or brought up from a since-deleted workspace, leaves
# hive-* containers that compose no longer knows about — and those hold
# bind-mounted data files open, which blocks the next run's workspace cleanup.
leftovers=$(docker ps -aq --filter "name=^/hive-")
if [ -n "$leftovers" ]; then
  echo "Removing leftover hive-* containers:"
  docker ps -a --filter "name=^/hive-" --format '  {{.Names}} ({{.Status}})'
  # shellcheck disable=SC2086  # one id per line; word splitting is the point
  docker rm -f $leftovers
fi
exit 0
