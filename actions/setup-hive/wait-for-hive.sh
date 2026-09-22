#!/usr/bin/env bash
# Polls Hive's HTTPS entrypoint until it answers, then exits 0. Any 2xx/3xx/4xx
# counts as up: the stack is serving, and an unauthenticated GET of / is
# expected to redirect or refuse. Only 5xx and a dead socket (curl failing,
# which yields "000") mean "not ready yet".
#
# Env:
#   HIVE_HOSTNAME   host to poll over HTTPS (required)
#   WAIT_ATTEMPTS   poll count, 5s apart (required)
set -uo pipefail

: "${HIVE_HOSTNAME:?HIVE_HOSTNAME is required}"
: "${WAIT_ATTEMPTS:?WAIT_ATTEMPTS is required}"

for i in $(seq 1 "$WAIT_ATTEMPTS"); do
  code=$(curl -ks -o /dev/null -w "%{http_code}" "https://${HIVE_HOSTNAME}/" || true)
  # curl always writes a code, but a missing binary would leave this empty
  # and turn the comparisons below into a bash error on every attempt.
  code=${code:-000}
  if [ "$code" -ge 200 ] && [ "$code" -lt 500 ]; then
    echo "Hive is up (HTTP $code)"
    exit 0
  fi
  echo "Attempt $i/$WAIT_ATTEMPTS - Hive not ready yet (HTTP $code), waiting 5s..."
  sleep 5
done
echo "::error::Hive failed to become ready in time"
exit 1
