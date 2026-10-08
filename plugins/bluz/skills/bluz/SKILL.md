---
name: bluz
description: How to drive the Bluz scheduling/curriculum app via the `bluz` CLI — auth, every command group, payload shapes, output parsing, known server bugs. Use for any user request to read/write Bluz data (rooms, courses, outsiders, reservations, iterations, calendar events, drafts/snapshots, gantt curriculum tree, the cut pipeline, settings, custom colours, Hive reference data, Google Calendar) without touching app or CLI source.
tags: [bluz, cli, api, gantt, scheduling]
---

# Bluz CLI

`bluz` is a Python/Typer CLI that talks to the same `/api/*` surface as the Bluz
web UI. This skill is self-sufficient — do not read `cli/bluz/*` or
`ui/src/api-*` source to use the tool; everything needed is below.

## Setup / auth

```bash
# No Bluz checkout? Install from the org's public pip index (the plugin's
# SessionStart hook already does this for you):
pip install bluz --index-url https://system-b90.github.io/.github/pypi/

# From a Bluz checkout instead:
pip install ./cli          # once, from repo root

bluz login                 # interactive: opens browser, or paste next-auth session token
```

Headless/agent use — skip the interactive prompt entirely:

```bash
bluz --url https://bluz.example.com --token <session-token> iterations list
# or env vars: BLUZ_URL, BLUZ_TOKEN, BLUZ_INSECURE (a local .env is auto-loaded)
```

Config precedence (first wins): CLI flag > env var > config file (`bluz auth config` shows the file path, URL, masked token).

`bluz auth hive-status` reports whether the server can reach Hive — check it first when logins or Hive-backed data fail, before blaming the CLI.

## Global flags

- `--json` — emit machine-readable JSON instead of a Rich table. **Always use this for scripting/agent parsing.**
- `--quiet` / `-q` — suppress success/warning chatter (stderr); only data (stdout) and hard errors remain. Use for chaining.
- `--url`, `--token`, `--insecure/--secure` — override config for one call.
- `--version`

Global flags are accepted before *or* after the subcommand — `bluz gantt curriculums list --json` and `bluz --json gantt curriculums list` both work.

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
bluz iterations sync-hive <id>                # re-snapshot Hive module/subject/room names
bluz iterations delete <id> --yes
```
Calendar reads/writes target the current iteration unless `--iteration/--it <id>` is passed (`bluz events`, `bluz calendar drafts`, `bluz calendar snapshots`, `bluz calendar export-ics`). Writes to a past iteration are rejected server-side.

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
bluz settings get-schedule          # shortcut for key "schedule"
bluz settings set-schedule --value '<json>'
```

### `bluz personal` — per-user settings
```bash
bluz personal get
bluz personal set [--groups a,b --instructors a,b --favorite-outsiders a,b]
bluz personal set [--google-enabled|--no-google-enabled] [--google-all-events|--no-google-all-events]
bluz personal set --data '<full json>'      # bypasses the merge, writes verbatim
```
The endpoint replaces the whole document; field flags are merged onto the current value first, `--data` is not.

### `bluz calendar` — shared drafts, snapshots, ICS export
```bash
bluz calendar drafts list [--iteration ID]
bluz calendar drafts get <id>
bluz calendar drafts create --label "..." (--events '<json array>' | --events-file f.json)
bluz calendar drafts update <id> [--label "..."] (--events ... | --events-file ...)
bluz calendar drafts delete <id> --yes

bluz calendar snapshots list [--iteration ID]
bluz calendar snapshots get <id>
bluz calendar snapshots create --label "..." (--events ... | --events-file ...)
bluz calendar snapshots restore <id> --yes     # archives live events in the snapshot's range
bluz calendar snapshots delete <id> --yes

bluz calendar export-ics --start ISO --end ISO [--output f.ics]   # max 366-day range
```
Drafts and snapshots both take a full events array — build it from `bluz --json events list ...`. Writes to a non-current iteration are rejected server-side.

### `bluz colors` — custom event colours
```bash
bluz colors list
bluz colors get <id>
bluz colors create --name "..." --hex "#3f51b5" [--id <uuid>]   # id is minted if omitted
bluz colors update <id> [--name --hex]                           # unset fields carry over
bluz colors delete <id> --yes
```

### `bluz hive` — read-only Hive LMS reference data
```bash
bluz hive users | students | classes | subjects | modules | rooms
bluz hive lessons [--module-id X --program-ids a,b]
```
These proxy Bluz's `/api/hive/*` routes. Read-only — never try to write to Hive through them.

### `bluz integrations google` — Google Calendar
```bash
bluz integrations google status          # configured (server-side) + connected (this user)
bluz integrations google connect --code <gis-authorization-code>
bluz integrations google sync            # two-way, 90-day window
bluz integrations google disconnect --yes
```
`connect` needs the authorization code from the browser-side Google Identity Services popup — there is no terminal-only OAuth flow. On deployments without Google credentials, `status` reports `configured: false` and everything else fails by design (Bluz must work fully offline).

### `bluz gantt` — curriculum/scheduling engine tree

Hierarchy: `curriculums` → `syllabuses` → `modules` → `events` (Gantt events, distinct from calendar events above). `weeks` → `days` are a parallel calendar structure under `curriculums`.

Every entity (`curriculums`, `syllabuses`, `modules`, `events`, `days`, `weeks`) shares:
```bash
bluz gantt <entity> list [--with-parents --limit N --offset N]   # → array of {id, title}; --with-parents adds the parent id
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
bluz gantt curriculums duplicate <id> [--overrides '<json>']
bluz gantt curriculums execution <id>          # תכנון מול ביצוע (plan vs. cut actuals)
bluz gantt curriculums recurrence-exceptions <id>
```

**The cut pipeline** — turns a published, iteration-linked curriculum into real schedule events:
```bash
bluz gantt curriculums cut-preview <id>        # dry run: dated occurrences, no gating, no writes
bluz gantt curriculums cut <id> [--force] --yes
bluz gantt curriculums cut-status <id>         # does the linked iteration hold live cut events?
bluz gantt curriculums pull-back <id> --yes    # soft-delete every event the cut generated
```
Cut gating failures are coded and write nothing: `draft`, `no-iteration`, `already-cut` (HTTP 409) and `invalid-plan` (HTTP 400). Always `cut-preview` before `cut`. `execution` on a not-yet-cut curriculum answers `{"events": {}}` with a 200 — that is not an error.

**Recurring gantt events** (only under `events`):
```bash
bluz gantt events duplicate <id> --module-id <m>            # copy gets the next indexed title
bluz gantt events except-occurrence <id> --curriculum-id <c> --day-id <d>   # drop one occurrence
bluz gantt events materialize <id> --curriculum-id <c> --module-id <m> --day-id <d>
```
`materialize` splits one occurrence into a standalone event *and* excepts the source from that day — use it when a single occurrence needs to differ; use `except-occurrence` when it should simply not happen.

## Scheduling guardrails — meal breaks are fixed points

Meal breaks are not ordinary events. Their times come from the `mealTimes`
setting and the rest of the day is built around them, so moving one silently
invalidates everything the humans already agreed on.

**Never move, resize, delete, unmap or re-map a meal break unless the user asks
for that break by name in the current request.** "Fit the schedule", "make room
for X", "rebalance the day" and the like are *not* permission — reflow the other
events around the break, and if the day genuinely cannot fit, say so and stop
rather than reclaiming the break's minutes.

How to recognise them:

- Calendar events (`bluz events`): `type` is `"הפסקה"` (`EventType.BREAK`).
- Gantt events (`bluz gantt events`): they live under the auto-seeded syllabus
  titled `"הפסקות"`; the three seeded titles are `"ארוחת בוקר"` (breakfast),
  `"הפסקת צהריים"` (lunch) and `"ארוחת ערב"` (dinner).
- Their intended times live in `bluz settings get mealTimes`
  (`breakfastTime` / `lunchTime` / `dinnerTime`, `"HH:mm"`).

Lunch and dinner are the ones users care about most — they are long enough that
a scheduler is tempted to raid them. Don't.

To change a break time deliberately, change the setting (`bluz settings set
mealTimes --value '{...}'`) rather than dragging the individual events, so every
day stays consistent.

## Known server bugs (not CLI bugs — don't waste time debugging the CLI for these)

None currently open. The two that used to live here — [#309](https://github.com/System-B90/Bluz/issues/309) (`weeks`/`days` list 500) and [#310](https://github.com/System-B90/Bluz/issues/310) (no parent id on gantt list/get) — are both fixed and closed. `weeks`/`days` now label by `number`/`dayIndex`, and parent ids are available via `bluz gantt <entity> list --with-parents`.

If a command fails in a way that looks server-side, check the repo's open issues before assuming a CLI bug.

## Quick recipes

```bash
# Find a room id by name
bluz rooms list --json | jq -r '.[] | select(.name=="חדר 101") | .id'

# Inspect a full curriculum tree (syllabuses → modules → events, weeks → days) in one call
bluz gantt curriculums get <id> --json

# Which syllabus is each module under?
bluz gantt modules list --with-parents --json | jq -r '.[] | "\(.id) \(.syllabusId)"'

# Snapshot the current week before a risky bulk edit, then restore it
bluz --json events list --start 2026-01-05T00:00:00Z --end 2026-01-12T00:00:00Z > week.json
bluz calendar snapshots create --label "pre-edit" --events-file week.json
bluz calendar snapshots restore <snapshot-id> --yes

# Dry-run a cut, then commit it
bluz gantt curriculums cut-preview <id> --json | jq '.[] | .startDate'
bluz gantt curriculums cut <id> --yes
```
