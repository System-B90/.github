#!/usr/bin/env bash
# Host-side manager for the persistent, shared Hive instance on the
# mks90-laptop-wsl runners. Called by actions/shared-hive-acquire and
# actions/shared-hive-release; also usable by hand on the host.
#
#   hive-shared.sh bootstrap <hive-stack-dir>   (re)create the instance + baseline
#   hive-shared.sh ensure                       start it if stopped, fail if absent
#   hive-shared.sh reset                        restore the baseline (clean state)
#   hive-shared.sh wait [attempts]              wait for https://hive.org to answer
#   hive-shared.sh status
#
# "Clean" means: the Hive database is a byte-for-byte copy of the baseline taken
# right after bootstrap, and Redis is empty. The baseline is a Postgres template
# database (CREATE DATABASE ... TEMPLATE), so a reset is a file copy inside the
# cluster and takes seconds, not a dump/restore.
#
# Media and course-dir bind mounts are NOT reset — consumers must only run
# non-destructive tests against this instance.
set -euo pipefail

HIVE_SHARED_HOME="${HIVE_SHARED_HOME:-$HOME/hive-shared}"
STACK="$HIVE_SHARED_HOME/stack"
STATE="$HIVE_SHARED_HOME/state"
# Project name "hive" keeps the network at hive_hive-net, which is what
# consumers (e.g. peek-a-boo's ui container) join to reach hive.org.
PROJECT=hive
BASELINE_DB=hive_ci_baseline

compose() { docker compose -p "$PROJECT" --project-directory "$STACK" -f "$STACK/docker-compose.yaml" "$@"; }
psql_admin() { compose exec -T database psql -v ON_ERROR_STOP=1 -U root -d postgres -Atc "$1"; }
# Root inside a throwaway container, for files owned by container uids (the
# runner user has no passwordless sudo). Uses a Hive image so nothing extra is
# pulled — pulls from an SSH session can trip Docker Desktop's cred helper.
as_root() { docker run --rm -v "$1" --entrypoint sh hive/redis:latest -c "$2"; }
log() { echo "[hive-shared] $*"; }

wait_db() {
  local cid
  cid=$(compose ps -q database)
  for _ in $(seq 1 120); do
    if [ "$(docker inspect --format '{{.State.Health.Status}}' "$cid" 2>/dev/null)" = healthy ] &&
      docker exec "$cid" pg_isready -h 127.0.0.1 -p 5432 >/dev/null 2>&1; then
      return 0
    fi
    sleep 5
  done
  log "Postgres did not become healthy"; docker logs --tail 100 "$cid" || true
  return 1
}

cmd_wait() {
  local attempts="${1:-90}" code
  for _ in $(seq 1 "$attempts"); do
    code=$(curl -ks -o /dev/null -w '%{http_code}' https://hive.org/api/core/ || true)
    if [ "$code" -ge 200 ] 2>/dev/null && [ "$code" -lt 500 ]; then
      log "Hive is answering (HTTP $code)"; return 0
    fi
    sleep 5
  done
  log "Hive did not answer at https://hive.org"; return 1
}

app_services() {
  # Everything except the datastores. These hold DB connections, so they are
  # stopped while the database is swapped.
  compose config --services | grep -vxE 'database|redis'
}

cmd_bootstrap() {
  local src="${1:?usage: bootstrap <hive-stack-dir>}"
  [ -f "$src/docker-compose.yaml" ] || { log "$src has no docker-compose.yaml"; exit 1; }

  log "Tearing down any previous instance"
  if [ -f "$STACK/docker-compose.yaml" ]; then compose down -v --remove-orphans || true; fi
  # Bind-mounted data (db/, media/) is owned by container uids; remove it as root
  # through Docker since the runner user has no passwordless sudo.
  if [ -d "$HIVE_SHARED_HOME" ]; then
    as_root "$HIVE_SHARED_HOME:/w" 'rm -rf /w/stack /w/state'
  fi
  mkdir -p "$STACK" "$STATE"
  cp -a "$src/." "$STACK/"

  cat >"$STACK/.env.override" <<'EOF'
HIVE_CORE_WORKERS=2
HIVE_CORE_THREADS=2
HIVE_NGINX_WORKERS=1
EOF
  mkdir -p "$STACK/db" "$STACK/media"
  as_root "$STACK/db:/d" "chown 999:999 /d"

  log "Starting datastores"
  compose up -d database redis
  wait_db
  log "Starting the stack"
  compose up -d || compose up -d

  compose exec -T core python manage.py migrate
  compose exec -T core python manage.py collectstatic --noinput
  compose exec -T database sh /update.sh
  compose exec -T core python manage.py service_accounts
  compose exec -T core python manage.py load_tags
  compose exec -T -e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_PASSWORD=Password1 \
    -e DJANGO_SUPERUSER_EMAIL=admin@hive.org core python manage.py createsuperuser --noinput
  compose exec -T core python manage.py load_programs
  # Peek-a-boo authenticates through the 'api' service account; pin its
  # password in the baseline so no consumer has to mutate it per run.
  compose exec -T core python manage.py shell -c \
    "from django.contrib.auth import get_user_model as g; u=g().objects.get(username='api'); u.set_password('Password1'); u.save()"

  local db; local -a svcs
  db=$(compose exec -T core python manage.py shell -c \
    "from django.conf import settings; print(settings.DATABASES['default']['NAME'])" | tr -d '\r' | tail -1)
  [ -n "$db" ] || { log "Could not determine Hive's database name"; exit 1; }
  echo "$db" >"$STATE/dbname"
  cp "$src/HIVE_SHA" "$STATE/hive_sha" 2>/dev/null || true

  log "Taking baseline of database '$db'"
  mapfile -t svcs < <(app_services)
  compose stop "${svcs[@]}"
  psql_admin "DROP DATABASE IF EXISTS $BASELINE_DB WITH (FORCE)"
  # A template must have no other sessions; the app services are stopped, but
  # powersync/grafana-style clients may linger.
  psql_admin "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname='$db' AND pid<>pg_backend_pid()" >/dev/null
  psql_admin "CREATE DATABASE $BASELINE_DB TEMPLATE \"$db\""
  compose up -d
  date -u +%FT%TZ >"$STATE/baseline_at"
  cmd_wait
  log "Bootstrap complete"
}

cmd_ensure() {
  if [ ! -f "$STATE/dbname" ] || [ ! -f "$STACK/docker-compose.yaml" ]; then
    log "No bootstrapped instance under $HIVE_SHARED_HOME"; exit 3
  fi
  compose up -d database redis
  wait_db
  if [ -z "$(psql_admin "SELECT 1 FROM pg_database WHERE datname='$BASELINE_DB'")" ]; then
    log "Baseline database '$BASELINE_DB' is missing"; exit 3
  fi
  compose up -d
}

cmd_reset() {
  local db owner; local -a svcs
  db=$(cat "$STATE/dbname")
  log "Restoring '$db' from baseline"
  mapfile -t svcs < <(app_services)
  compose stop -t 5 "${svcs[@]}"
  owner=$(psql_admin "SELECT pg_get_userbyid(datdba) FROM pg_database WHERE datname='$db'")
  psql_admin "DROP DATABASE IF EXISTS \"$db\" WITH (FORCE)"
  psql_admin "CREATE DATABASE \"$db\" TEMPLATE $BASELINE_DB OWNER \"${owner:-root}\""
  compose exec -T redis redis-cli FLUSHALL >/dev/null
  compose up -d
  cmd_wait
}

cmd_status() {
  compose ps --format '{{.Name}}\t{{.Status}}' || true
  for f in dbname hive_sha baseline_at; do
    [ -f "$STATE/$f" ] && echo "$f: $(cat "$STATE/$f")"
  done
}

sub="${1:-status}"; shift || true
case "$sub" in
  bootstrap) cmd_bootstrap "$@" ;;
  ensure) cmd_ensure ;;
  reset) cmd_reset ;;
  wait) cmd_wait "$@" ;;
  status) cmd_status ;;
  *) echo "unknown command: $sub" >&2; exit 2 ;;
esac
