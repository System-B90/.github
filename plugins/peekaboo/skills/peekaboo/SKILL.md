---
name: peekaboo
description: How to drive the Peek-a-boo student-monitoring app via the `peekaboo` CLI — auth, every command, output parsing, quirks. Use for any user request to read or change Peek-a-boo data or act on it (student roster / mentees, classes, opening a student's VNC screen, native-VNC connection details, TightVNC client install commands, posting to the tweet channel with a screenshot or recording, server settings) without touching app or CLI source.
tags: [peekaboo, peek-a-boo, cli, vnc, students, monitoring]
---

# Peek-a-boo CLI

`peekaboo` is a Python/Typer CLI that talks to the same `/api/*` routes as the
Peek-a-boo web UI. Everything the UI can do has a command. This skill covers
everything you need, so you don't have to read `cli/peekaboo/*` or `src/app/api/*`.

## Setup / auth

```bash
# The plugin's SessionStart hook installs it; manually:
pip install peekaboo --extra-index-url https://system-b90.github.io/.github/pypi/
# or, from a peek-a-boo checkout:
pip install ./cli

peekaboo login        # opens /cli-auth in the browser (Hive SSO), hands the session back
peekaboo auth whoami  # who the stored session belongs to
```

Headless/agent use without the interactive prompt:

```bash
PEEKABOO_URL=https://peekaboo.example.com PEEKABOO_TOKEN=<next-auth session token> peekaboo --json students list
```

The config comes from, in order of precedence: CLI flag, then env var (`PEEKABOO_URL`, `PEEKABOO_TOKEN`, `PEEKABOO_INSECURE`; a cwd `.env` is
read), then the config file. `peekaboo auth config` shows the file path, the URL and a masked token.
If the browser can't reach the CLI, `login` asks you to paste the handoff code shown on the page.
Use `--insecure` for self-signed dev certs (e.g. `https://peekaboo.dev`).

## Global flags (accepted before or after the subcommand)

- `--json` gives machine-readable output. **Always use it when parsing.**
- `-q` / `--quiet` keeps only data (stdout) and errors.
- `--url`, `--insecure/--secure`, `--timeout SECONDS`, `--version`.

Exit code `1` on API/auth/validation errors. A redirect to `/login` means the
session expired: run `peekaboo login` again.

## Commands

### Students (the dashboard / mentees page)
```bash
peekaboo students list [--mine | --mentor USERNAME] [--program NAME] [--status STATUS] [--wide] [--limit N --offset N]
peekaboo students get <username>          # full roster row
peekaboo students avatar <hiveId> -o face.png
```
Roster rows (`--json`) have these fields: `studentUsername, studentNumber, studentFirstName, studentLastName,
studentStatus, hiveId, hostname, queueName, programName, mentorUsername/FirstName/LastName,
currentExerciseName/Id, currentExerciseParentModuleId, …ParentModuleParentSubjectId, checkersBrief`.
The table view shows only a narrow column set unless you pass `--wide`; `--json` always includes every field.
`--mine` reads the logged-in user from `/api/auth/session` (this fails under login bypass, so pass `--mentor` there).

### Classes
```bash
peekaboo classes list
```

### VNC (student screens)
```bash
peekaboo vnc open <username> [--fullscreen] [--print]   # opens /vnc/<hostname> (or /fullscreen?username=)
peekaboo vnc info <username> [--reveal]                # host, port 5900, VNC password, websocket URL
peekaboo vnc install-command                           # raw PowerShell TightVNC installer (server-generated)
peekaboo vnc install-command --computer PC-01 [--username administrator] [--password P]
peekaboo vnc install-command --search-scope "OU=Classroom,DC=example,DC=com" [--password P]
```
Watching a screen itself needs a browser or a native VNC viewer: use `vnc info --reveal` for the viewer's connection details.
`--print` outputs the URL instead of launching a browser, which is what you want for agents.

### Tweet bot (Mattermost tweet channel)
```bash
peekaboo tweet "message **markdown**" [--attach screenshot.png|clip.webm]
```
Only image or video attachments are accepted, up to 12 MB.

### Settings (settings page)
```bash
peekaboo settings show [--defaults] [--reveal]   # secrets masked as <set> unless --reveal
peekaboo settings set KEY=VALUE [KEY=VALUE ...]  # only the given keys change
peekaboo settings reset --yes                    # restore all defaults
```
Keys: `VNC_CLIENT_PASSWORD, VNC_MASTER_PASSWORD, HIVE_HOSTNAME, HIVE_PASSWORD,
HIVE_POSTGRES_HOSTNAME, HIVE_API_USERNAME, HIVE_API_PASSWORD, HIVE_POSTGRES_USERNAME,
MATTERMOST_URL, MATTERMOST_ACCESS_TOKEN, TWEET_CHANNEL_ID`. Unknown keys are rejected.
**Always pass `--yes` to `reset`** in scripts, otherwise it blocks on a prompt.

### Misc
```bash
peekaboo env                                   # WEBSOCKET_URL, HIVE_HOSTNAME, ALLOW_LOGIN_BYPASS
peekaboo open [dashboard|mentees|fullscreen|settings] [--print]
peekaboo health                                # exits 0 only when /api/health says ok
peekaboo interactive                           # menu over every command (needs a TTY)
```

## Quick recipes

```bash
# Hostnames of everyone currently in the toilet queue
peekaboo --json students list --status Toilet | jq -r '.[].hostname'
# My mentees' current exercises
peekaboo --json students list --mine | jq -r '.[] | "\(.studentUsername)\t\(.currentExerciseName)"'
# Point TigerVNC at a student
peekaboo --json vnc info alice --reveal
# Change the tweet channel
peekaboo settings set TWEET_CHANNEL_ID=abc123
```
