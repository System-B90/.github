---
name: bluz-cli
description: How to drive the Bluz scheduling/curriculum app via the `bluz` CLI — auth, every command group, payload shapes, output parsing, known server bugs. Use for any user request to read/write Bluz data (rooms, courses, outsiders, reservations, iterations, events, gantt curriculum tree, settings) without touching app or CLI source.
tags: [bluz, cli, api, gantt, scheduling]
---

# Bluz CLI

`bluz` is a Python/Typer CLI that talks to the same `/api/*` surface as the Bluz
web UI. This skill is self-sufficient — do not read `cli/bluz_cli/*` or
`ui/src/api-*` source to use the tool; everything needed is below.

## Setup / auth

```bash
pip install ./cli          # once, from repo root
bluz login                 # interactive: opens browser, or paste next-auth session token
```

Headless/agent use — skip the interactive prompt entirely:

```bash
bluz --url https://bluz.example.com --token <session-token> iterations list
# or env vars: BLUZ_URL, BLUZ_TOKEN, BLUZ_INSECURE (a local .env is auto-loaded)
```

Config precedence (first wins): CLI flag > env var > config file (`bluz auth config` shows the file path, URL, masked token).

## Global flags

- `--json` — emit machine-readable JSON instead of a Rich table. **Always use this for scripting/agent parsing.**
- `--quiet` / `-q` — suppress success/warning chatter (stderr); only data (stdout) and hard errors remain. Use for chaining.
- `--url`, `--token`, `--insecure/--secure` — override config for one call.
- `--version`

## Output shape

- List commands return a JSON **array**. Every list command also accepts `--limit N` `--offset N` (client-side slicing — server has no pagination).
- Single-item commands (`get`, `create`, `update`) return a JSON **object**.
- Destructive commands (`delete`/`cancel`) print a `✓ ...` line to stdout on success (suppress with `--quiet`); exit code `0`.
- Exit code non-zero (`1`) on API/auth/validation error, or on an unconfirmed `delete` — **always pass `--yes`/`-y` for delete/cancel in scripts/agents** or it blocks on a prompt.
- Parse with `jq` (`bluz --json iterations list | jq -r '.[].id'`) or PowerShell `ConvertFrom-Json`.

## Command groups

### `bluz iterations` — bi-annual course runs
```bash
bluz iterations list [--limit N --offset N]
bluz iterations current                       # active/writable iteration
bluz iterations get <id>                      # e.g. 2026a
bluz iterations register <id> --label "..." [--db-name --hive-url --start-date --end-date --gantt-curriculum-id]
bluz iterations patch <id> [--label --hive-url --end-date --gantt-curriculum-id --current/--not-current]
bluz iterations set-current <id>
bluz iterations delete <id> --yes
```

### `bluz rooms` — custom + Hive-backed
```bash
bluz rooms list [--limit N --offset N]
bluz rooms get <id>                           # client-side filter, no server per-id route
bluz rooms create --name "..." [--description --id]
bluz rooms update <id> [--name --description]
bluz rooms delete <id> --yes
bluz rooms set-info <id> --source 0|1 --info '{"workstationCount":20,"lectureSeatCount":40,"lectureComfortable":true,"peAyin":false}'
```
Room source enum: `0` = Custom, `1` = Hive.

### `bluz courses`
```bash
bluz courses list [--limit N --offset N]
bluz courses get <id>
bluz courses create --name "..." [--color "#2196f3" --parent-id --instructor-ids '[123,456]' --id]
bluz courses update <id> [--name --color --parent-id --instructor-ids]
bluz courses delete <id> --yes
```

### `bluz reservations` — room bookings
```bash
bluz reservations list [--room-id --room-source 0|1 --from ISO --to ISO --limit N --offset N]
bluz reservations get <_id>                   # note: field is _id not id
bluz reservations create --room-id X --room-source 0|1 --start ISO --end ISO --reserver-type instructor|outsider --reserver-id X [--note]
bluz reservations cancel <_id> --yes
```

### `bluz outsiders` — external visitors
```bash
bluz outsiders list [--limit N --offset N]
bluz outsiders get <id>
bluz outsiders create --name "..." --phone "..." [--personal-number --id-number --release-date ISO --comment --id]
bluz outsiders update <id> [--name --phone --personal-number --id-number --release-date --comment]
bluz outsiders delete <id> --yes
```

### `bluz events` — calendar events (not Gantt events — see below)
```bash
bluz events list --start ISO --end ISO [--iteration ID --limit N --offset N]
bluz events get <id1,id2,...> [--iteration ID]
bluz events create --data '{...}'
bluz events update --data '{"id":"...", ...}'    # must include id in payload
bluz events delete <id> --yes
bluz events compare --start ISO --end ISO [--it-a ID --it-b ID]
```

### `bluz settings`
```bash
bluz settings list                  # static known keys only (no server enumeration route)
bluz settings get <name>
bluz settings set <name> --value '<json>'
bluz settings get-prayer            # shortcut for key "prayer-times"
bluz settings set-prayer --value '<json>'
```

### `bluz gantt` — curriculum/scheduling engine tree

Hierarchy: `curriculums` → `syllabuses` → `modules` → `events` (Gantt events, distinct from calendar events above). `weeks` → `days` are a parallel calendar structure under `curriculums`.

Every entity (`curriculums`, `syllabuses`, `modules`, `events`, `days`, `weeks`) shares:
```bash
bluz gantt <entity> list [--limit N --offset N]      # → array of {id, title}
bluz gantt <entity> get <id>                          # full item incl. sub-tree
bluz gantt <entity> get-many <id1,id2,...>             # → array of full items
bluz gantt <entity> create --data '<json>'
bluz gantt <entity> update <id> --data '<json patch>'
bluz gantt <entity> delete <id> --yes
```
`syllabuses`, `modules`, `events`, `days`, `weeks` (not `curriculums`) additionally have:
```bash
bluz gantt <entity> link <id> <new-parent-id>
bluz gantt <entity> unlink <id> <old-parent-id>
```
`modules`, `events` additionally have:
```bash
bluz gantt <entity> get-time <id> <container-id>
bluz gantt <entity> set-time <id> <container-id> <duration>
```
`syllabuses` additionally: `bluz gantt syllabuses reorder-modules <syllabus-id> <mod1,mod2,...>`
`modules` additionally: `bluz gantt modules reorder-events <module-id> <ev1,ev2,...>`

**Create payload field names** (pass via `--data '<json>'`; `id`/`title` are server-generated, don't send them):

- **curriculums**: `{"title": str, "description": str, "startDate": iso|null, "isDraft": bool, "isArchived": bool}`
- **syllabuses**: `{"curriculumId": str, "title": str, "hiveIds": [int], "shuffles": [str]?}`
- **modules**: `{"syllabusId": str, "title": str, "description": str, "hiveIds": [int], "shuffles": [str]?}`
- **weeks**: `{"curriculumId": str, "comment": str?, "weekendDuty": bool}` — `title`/`number` are server-generated; creating a week auto-creates its 7 days.
- **days**: `{"weekId": str, "dayIndex": int, "totalWorkingMinutes": int, "comment": str?}`
- **events** (Gantt events under a module): `{"moduleId": str, "title": str, "type": ..., "minimumDuration": int, "allocatedDuration": int, "orchestratorId": int|null, "recommendedLecturerIds": [str], "systemRequirements": [str], "roomRequirement": {...}, "recurrence": {...}}` — `roomRequirement`/`recurrence`/`type` are nested/enum shapes not worth memorizing: **run `bluz gantt events get <existing-id> --json` first and copy/adapt its shape** rather than guessing.

Curriculum-specific extras (only under `curriculums`):
```bash
bluz gantt curriculums export <id> [--output file.json]
bluz gantt curriculums export-excel <id> --output file.xlsx
bluz gantt curriculums import <exported-file.json>
bluz gantt curriculums constraints <id> [--syllabus-id --module-id]
bluz gantt curriculums mappings <id>
```

## Known server bugs (not CLI bugs — don't waste time debugging the CLI for these)

Check the linked issue's state before trusting either entry below — both may be fixed by the time you read this.

- **`bluz gantt weeks list` / `bluz gantt days list` return HTTP 500** as of [System-B90/Bluz#309](https://github.com/System-B90/Bluz/issues/309) (generic list query assumes every Gantt entity has a `title` column; `weeks`/`days` don't). Workaround: `bluz gantt curriculums get <id>` — its sub-tree includes weeks and their days directly (syllabuses do **not** carry weeks/days, only modules).
- **Modules don't expose parent `syllabusId`; events don't expose parent `moduleId`** as of [System-B90/Bluz#310](https://github.com/System-B90/Bluz/issues/310) (list or get). Workaround: walk down from the parent (`syllabuses get <id>` lists its `modules` ids; `modules get <id>` lists its `events` ids) rather than looking up a parent from a child id.

## Quick recipes

```bash
# Find a room id by name
bluz rooms list --json | jq -r '.[] | select(.name=="חדר 101") | .id'

# Inspect a full curriculum tree (syllabuses → modules → events, weeks → days) in one call
bluz gantt curriculums get <id> --json
```
