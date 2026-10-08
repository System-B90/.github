---
name: madash
description: How to drive the madash dashboard via the `madash` CLI — auth, every command, output parsing, quirks. Use for any user request to read or change madash state: the madrat message (including watching it live in the terminal), the call-to-Hadas board (calling students, marking told, removing calls), the daily journal, the system status board (services, Hive Prometheus, toilet queue, open helps), and Hive students/classes/avatars — without touching app or CLI source.
tags: [madash, cli, madrat, hadas, dashboard]
---

# madash CLI

`madash` is a Python/Typer CLI that talks to the same `/api/*` routes as the
madash web UI. Everything the UI can do has a command. This skill covers
everything you need, so you don't have to read `cli/madash/*` or `src/app/api/*`.

## Setup / auth

```bash
# The plugin's SessionStart hook installs it; manually:
pip install madash --extra-index-url https://system-b90.github.io/.github/pypi/
# or, from a madash checkout:
pip install ./cli

madash login          # opens /cli-auth in the browser (Hive SSO), hands the session back
madash auth whoami
```

Headless/agent use: `MADASH_URL`, `MADASH_TOKEN` (next-auth session token), `MADASH_INSECURE`
(a cwd `.env` is read). The config comes from, in order of precedence: CLI flag, then env, then the config file (`madash auth config`).
Use `--insecure` for self-signed dev certs (e.g. `https://madash.dev`).

## Global flags (accepted before or after the subcommand)

`--json` (always use it when parsing), `-q/--quiet`, `--url`, `--insecure/--secure`,
`--timeout`, `--version`. Exit code `1` on errors. madash has **no database**, so all state
(madrat text, calls, journal) lives in the server process and is lost when it restarts.

## Commands

### Madrat message
```bash
madash madrat get [--plain]                 # rendered Markdown; --plain = raw text; --json = JSON string
madash madrat set "new **message**"         # replaces it for every viewer immediately
madash madrat set --file msg.md             # or --file - to read stdin
madash madrat clear
madash madrat watch [-n 2] [--plain]        # LIVE: redraws in place on every change, Ctrl+C to stop
madash --json madrat watch                  # one JSON line {"at","text"} per change (for piping)
```
`watch` polls `/api/madrat` every `-n` seconds (default 2, minimum 0.2). If a poll fails,
the last message stays on screen and the footer shows "retrying". **Agents:** `watch` runs
until interrupted; use `get` for a one-shot read.

### Call-to-Hadas board
```bash
madash hadas list [--state requested|told]
madash hadas call <student>... --reason "..." [--expires +90m|+2h|HH:MM|ISO] [--group]
madash hadas told <callId>
madash hadas state <callId> requested|told
madash hadas remove <callId>
```
You can pick a student by Hive id, student number (`bisId`) or username. If none match, or more than one does,
the command aborts before it calls anyone. `--expires` defaults to 6 hours from now, rounded up to 5 minutes (the UI's default);
an `HH:MM` that has already passed today means tomorrow. `--group` makes one shared call instead of one per student.
Calling the same student with the same reason and expiry twice is rejected by the server (the message comes back in Hebrew).
Get the `callId` values from `madash --json hadas list` (the object keys).

### Journal
```bash
madash journal get [-d YYYY-MM-DD]          # default: today
madash journal rename "name" [-d DATE]
madash journal done <taskId> [-d DATE]
madash journal undo <taskId> [-d DATE]
madash journal update journal.json          # save a whole journal (shape = `journal get --json`)
```
Past days are read-only, and the CLI refuses to write them.

### Status board
```bash
madash status services        # bluz / peekaboo health: state up|degraded|down|unconfigured, latency
madash status prometheus      # {configured, reachable, overloaded}
madash status toilet-queue    # {waiting, out}
madash status open-helps      # {count}
madash status all
```

### Hive data
```bash
madash hive students [--room NAME] [--status S] [--raw]   # {hiveId, username, name, bisId, room, status}
madash hive classes                                       # rooms ("Room") and groups ("Student Group")
madash hive avatar <hiveId> -o face.jpg
```

### Misc
```bash
madash open [dashboard|journal] [--print]
madash health                  # exit 0 only when /api/health says ok
madash auth ws-ticket          # session-server WebSocket ticket (debugging live sync)
madash interactive             # menu over every command (needs a TTY)
```

## Quick recipes

```bash
# Call two students for 30 minutes
madash hadas call alice 102 --reason "שיחה עם המפקד" --expires +30m
# Mark every requested call as told
madash --json hadas list --state requested | jq -r 'keys[]' | xargs -n1 madash -q hadas told
# Put a file on the madrat board and watch it
madash madrat set --file announcements.md && madash madrat watch
```
