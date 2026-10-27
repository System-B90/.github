---
name: pyhive
description: How to read and change Hive LMS data with the `pyhive` CLI and the PyHive Python SDK — sign-in without a browser, every command, JSON output shapes, SDK filters and model helpers, known quirks. Use for any request to look up or modify Hive programs, subjects, modules, exercises, assignments, users/students, classes, the schedule or help requests, or to write a Python script against a Hive server.
---

# PyHive for agents

`pyhive` is a Typer CLI over the PyHive SDK (`pip` package `PyHiveLMS`, import
name `pyhive`). This page is self-contained for everyday work. Do not read the
PyHive source to use it.

| Need                                   | Read                                                   |
| -------------------------------------- | ------------------------------------------------------ |
| Every command, option and output shape | [cli.md](cli.md) · `pyhive docs show cli`              |
| Writing a Python script against Hive   | [sdk.md](sdk.md) · `pyhive docs show sdk`              |
| A working script to start from         | [examples.md](examples.md) · `pyhive examples list`    |

## CLI or SDK?

The CLI covers **list / get / delete** for programs, subjects, modules,
exercises, assignments, classes and users, plus creating staff users. Anything
else — filtering, creating course content or students, the schedule, help
requests, bulk changes, joins across resources — is a short SDK script. Run it
inline:

```bash
python - <<'EOF'
from pyhive.cli.client_factory import default_hive_url, get_hive_client
client = get_hive_client(default_hive_url(), verify=False)  # same server and sign-in as the CLI
for module in client.get_modules(parent_subject__id=12):
    print(module.id, module.order, module.name)
EOF
```

## Setup

```bash
pyhive version            # installed? prints the PyHive version
pip install PyHiveLMS --index-url https://system-b90.github.io/.github/pypi/   # if not
```

## Signing in without a browser

With no credentials, every command falls back to **SSO, which opens a browser
and blocks** until someone signs in. An agent must supply credentials. The CLI
tries, in order:

1. `-u USER -p PASS` (root options)
2. `-t TOKEN` / `--token TOKEN` (root option)
3. the `HIVE_ACCESS_TOKEN` environment variable
4. the OS keyring cache from `pyhive auth login` (or `--cache-token`), used
   only for the server it was saved for
5. SSO in the browser

Check first with `pyhive --json auth status`: `{"hive_url": ..., "token_cached":
true}` means commands already sign in silently to that server. Otherwise ask the
user to run this once in their own terminal (in Claude Code:
`! pyhive auth login`). It asks for the Hive URL, signs in through the browser,
and stores the URL and both tokens in the OS keyring. Every later `pyhive` call,
and `get_hive_client(default_hive_url(), ...)` in scripts, then uses that server,
signs in silently and refreshes the token itself. Never run `auth login`
yourself: it prompts, then blocks on the browser.

Scripts reuse the same chain through `get_hive_client()` (as in the snippet
above), so they need no credentials of their own.

## Rules for calling the CLI

- **Always pass `--json`.** It works anywhere on the line. stdout then holds one
  JSON document; progress lines (`Fetching …`) are suppressed.
- **`-u`, `-p`, `-t` go before the group**: `pyhive -t "$TOKEN" --json users list`.
  After the group they fail with `No such option`.
- **`--hive-url` and `--verify` go after the leaf command**:
  `pyhive --json programs list --hive-url https://hive.example`. Placed after the
  group (`pyhive programs --hive-url … list`) they are **silently ignored**.
  A `--hive-url` other than the cached server skips the cached token and
  falls back to SSO, so leave it out unless the user names another server.
- Defaults: the server cached by `auth login`, else `https://hive.org`; TLS
  verification **off**.
- Exit code `0` on success, `1` on any error. In `--json` mode the error is JSON
  on **stderr**: `{"error": "...", "details": "..."}`.
- `delete` commands **do not prompt**. Confirm with the user before running
  one. Deleting a subject also deletes its modules and exercises.

## Commands

```bash
pyhive --json programs list                 # {"programs": [...]}
pyhive --json programs get 2                # {"program": {...}}
pyhive --json programs delete 2             # {"deleted_program_id": 2, "status": "success"}
# Same list/get/delete for: subjects, modules, exercises, classes
pyhive --json assignments list | get ID     # no delete
pyhive --json users list | delete ID        # no get
pyhive --json users create USERNAME --password PW --clearance checker --gender female \
    [--first-name --last-name --number --status --teacher/--no-teacher --confirmed/--no-confirmed]

pyhive --json auth status                   # {"hive_url", "token_cached", "env_token_set"}; no network
pyhive auth login | logout                  # user runs login (prompts + browser); logout clears the cache
pyhive --json token [--cache-token]         # SSO in the browser → {"access_token", "refresh_token", "expires_at"}
pyhive --json register NAME REDIRECT_URI    # register an SSO client app → client_id/secret
pyhive --json version | versions            # PyHive version / Hive versions it supports

pyhive docs [show PAGE | path | install-skill]
pyhive examples [list | show NAME | run NAME [ARGS...]]
```

`list` and `get` return every field Hive sends, under **Hive's wire names**:
related objects are plain ids under `program`, `checker`, `mentor`,
`parent_subject`, `parent_module`, `user`, `exercise`, and `classes`/`users` are
id lists. The SDK names the same fields `program_id`, `mentor_id`, `class_ids`
and so on.

Enum names accepted by `users create` (any case):
`--clearance` `HANICH` (student) · `CHECKER` · `SEGEL` (staff) · `ADMIN`;
`--gender` `MALE` · `FEMALE` · `NONBINARY`; `--status` defaults to `PRESENT`.
`users create` cannot make a student — a student needs a program and a number,
and the command has no `--program`. Use `client.create_student(...)` in the SDK.

Parse output with `jq` or Python:

```bash
pyhive --json subjects list | jq -r '.subjects[] | "\(.id)\t\(.symbol)\t\(.name)"'
pyhive --json users list | python -c "import json,sys; print(len(json.load(sys.stdin)['users']))"
```

## SDK essentials

```python
from pyhive import HiveClient
from pyhive.types import AssignmentStatusEnum, ClearanceEnum

with HiveClient("admin", "password", "https://hive.org", verify=False) as client:
    program = client.get_program(2)
    for subject in program.get_subjects():          # list endpoints return generators
        for module in subject.get_modules():
            print(subject.symbol, module.order, module.name)

    student = client.get_student(number=1234)        # or name="First Last"; None if no single match
    done = [a for a in client.get_assignments(for_user=student)
            if a.assignment_status == AssignmentStatusEnum.DONE]
```

- List methods (`get_*s`) return **generators**: wrap in `list(...)` to index,
  count or reuse them.
- Methods accept an **id or a model** wherever they take a related object
  (`get_assignments(for_user=student)` or `for_user=13`).
- Relations on models (`assignment.user`, `user.mentor`, `class_.users`) are
  lazy and cost **one request each**. In loops, fetch the table once
  (`{u.id: u for u in client.get_users()}`) and join by id.
- Enums live in `pyhive.types`; compare with members, not strings.
- `*_name=` filters (`subject_name=`, `module_name=`, …) are **exact** matches.
  Passing two filters that contradict each other raises `AssertionError`.
- Errors: HTTP 400 → `ValueError("HTTP 400 Error: {...}")` with Hive's message;
  other HTTP errors → `httpx.HTTPStatusError`; a failed delete →
  `RuntimeError`; an unlisted Hive version → `UnverifiedHiveVersionError`
  (pass `skip_version_check=True` to try anyway).

Full method reference and recipes: [sdk.md](sdk.md).

## Known quirks

- `get_user_me()` raises `NotImplementedError`.
- Staff accounts can only open **chat** help requests
  (`client.create_chat(with_user=…)`); `create_help_request` with another type
  is rejected with `Staff may only create staff chats`.
- `get_student(name=…)` matches the full name, display name or username first,
  then the first name alone. It returns `None` when nothing matches and raises
  `RuntimeError` when several users share that first name.
