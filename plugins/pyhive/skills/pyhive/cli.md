# CLI reference

`pyhive` is installed with the `PyHiveLMS` package. It is built on the
[Python SDK](sdk.md), so anything a command does, a script can do too. The
CLI covers the everyday reads and deletes; the SDK covers everything else.

```bash
pyhive --help              # command groups
pyhive programs --help     # one group
pyhive docs show cli       # this page, in the terminal
```

## Command line shape

```text
pyhive [-u USER -p PASS | -t TOKEN] [--json] [--cache-token] GROUP COMMAND [ARGS] [--hive-url URL] [--verify]
```

| Option                | Where it goes                 | What it does                                                        |
| --------------------- | ----------------------------- | ------------------------------------------------------------------- |
| `-u`, `--username`    | before the group              | Hive username (with `-p`)                                           |
| `-p`, `--password`    | before the group              | Hive password (with `-u`)                                           |
| `-t`, `--token`       | before the group              | Hive access token                                                   |
| `--json`              | anywhere                      | Print one JSON document on stdout instead of text                   |
| `--cache-token`       | anywhere                      | Save the server and token in the OS keyring for later calls         |
| `--hive-url URL`      | after the command             | Server to talk to. Default: the cached one, else `https://hive.org` |
| `--verify/--no-verify`| after the command             | Verify TLS certificates. Default `--no-verify`                      |

!!! warning "Option placement matters"
    `-u`, `-p` and `-t` belong to the root command: after the group they fail
    with `No such option`. `--hive-url` and `--verify` belong to the final
    command: `pyhive programs --hive-url URL list` accepts the option but
    **ignores** it and talks to the default server. Write
    `pyhive programs list --hive-url URL`.

## Signing in

Sign in once:

```bash
pyhive auth login
```

It asks for the Hive URL (Enter keeps the one shown), opens the browser on
Hive's sign-in page, and saves the URL, the access token and the refresh token
in the OS keyring (service `pyhive_cli`). Later commands talk to that server by
default, sign in without a browser, and refresh the access token when it
expires. Anyone who can read your keyring can act as you, so only do this on
your own machine.

```bash
pyhive auth login --hive-url https://hive.example   # no prompt
pyhive auth status                                  # cached server, and whether a token is cached
pyhive auth logout                                  # forget the server and the tokens
```

`auth status` only reads the keyring. It does not check that the token still
works.

Every command that talks to Hive picks the first credentials it finds:

1. `-u USER -p PASS`
2. `-t TOKEN`
3. the `HIVE_ACCESS_TOKEN` environment variable
4. the keyring cache from `pyhive auth login` or `--cache-token`, if it was
   saved for the same server the command talks to
5. otherwise, SSO: a browser opens on Hive's sign-in page and the command
   waits for you to finish

`--cache-token` on any command saves the server it used and the token it ended
up with, the same way `auth login` does. Without `--hive-url`, commands use the
cached server, or `https://hive.org` if none is cached. Giving `--hive-url` for
a different server ignores the cached token instead of sending it there.

A token from `-t` or `HIVE_ACCESS_TOKEN` cannot be refreshed: when it expires,
get a new one with `pyhive token`.

## Output

Text mode prints progress lines and aligned lists for people. With `--json`,
stdout holds exactly one JSON document:

| Command kind | JSON on stdout                                               |
| ------------ | ------------------------------------------------------------ |
| `list`       | `{"programs": [{...}, ...]}` — key is the group name          |
| `get`        | `{"program": {...}}` — key is the singular                    |
| `delete`     | `{"deleted_program_id": 2, "status": "success"}`              |
| error        | nothing on stdout; `{"error": "...", "details": "..."}` on **stderr** |

The exit code is `0` on success and `1` on any error. Lists are sorted by `id`.

Objects carry every field Hive returns, under Hive's own field names. Related
objects appear as ids: `"program": 2`, `"mentor": 1`, `"classes": [1, 3]`.
(The SDK models expose the same values as `program_id`, `mentor_id`,
`class_ids`.)

```bash
pyhive --json subjects list | jq -r '.subjects[] | "\(.id)\t\(.symbol)\t\(.name)"'
pyhive --json users list | jq '[.users[] | select(.clearance == 1)] | length'   # students
```

## Course content

Programs contain subjects, subjects contain modules, modules contain exercises.

```bash
pyhive programs list
pyhive programs get 2
pyhive programs delete 2

pyhive subjects list
pyhive subjects get 12
pyhive subjects delete 12        # also deletes the subject's modules and exercises

pyhive modules list
pyhive modules get 40
pyhive modules delete 40

pyhive exercises list
pyhive exercises get 7
pyhive exercises delete 7
```

Running a group with no command runs its `list`: `pyhive subjects` is
`pyhive subjects list`.

!!! danger "Deletes do not ask for confirmation"
    `delete` commands run immediately and cannot be undone.

The CLI does not create or edit course content. Use the SDK:
`program.create_subject(...)`, `subject.create_module(...)`,
`module.create_exercise(...)` — see the
[`build_module` example](examples.md#build_module).

## Assignments

An assignment is one student's copy of one exercise.

```bash
pyhive assignments list
pyhive assignments get 1234
```

`list` returns every assignment the account can see. To filter (by student,
mentor, module, subject…), use `client.get_assignments(...)` in the SDK.

## Classes

A class is either a room or a student group (`"type": "Room"` /
`"Student Group"`).

```bash
pyhive classes list
pyhive classes get 3
pyhive classes delete 3
```

## Users

```bash
pyhive users list
pyhive users delete 15
pyhive users create jdoe --password 'S3cret!' --clearance checker --gender female \
    --first-name Jane --last-name Doe
```

`users create` options:

| Option                          | Values                                                                        |
| ------------------------------- | ----------------------------------------------------------------------------- |
| `USERNAME`                      | required argument                                                             |
| `--password`                    | prompted (hidden) if omitted — always pass it in scripts                      |
| `--clearance`                   | required: `HANICH` (student), `CHECKER`, `SEGEL` (staff), `ADMIN`, any case  |
| `--gender`                      | required: `MALE`, `FEMALE`, `NONBINARY`                                       |
| `--status`                      | `PRESENT` (default), `RAISED_HAND`, `TOILET`, `HOME`, `MEDICAL`, …            |
| `--number`                      | identification number                                                         |
| `--first-name`, `--last-name`   |                                                                               |
| `--avatar-filename`             |                                                                               |
| `--teacher/--no-teacher`        |                                                                               |
| `--confirmed/--no-confirmed`    |                                                                               |

On success the JSON is `{"user": {...}, "status": "created"}`.

!!! note "Students need the SDK"
    A student (`HANICH`) must have a program and a number, and `users create`
    has no `--program` option, so it can only create staff.
    Create students with `client.create_student(username, password, gender,
    number=..., program=...)`.

## Sign-in helpers

```bash
pyhive token                        # SSO in the browser, prints the access token
pyhive --json token                 # {"access_token", "refresh_token", "expires_at"}
pyhive token --cache-token          # ...and saves the server and both tokens, like `auth login`

pyhive register "My service" http://localhost:5000/api/auth/callback/hive
```

`register` creates an SSO (OAuth) client application on Hive and prints its
`client_id` and `client_secret`, for building another service that signs in
with Hive. It needs an account allowed to manage SSO applications.

## Versions

```bash
pyhive version       # this PyHive's version
pyhive versions      # every Hive release this PyHive is verified against
```

PyHive checks the server's version when it connects and refuses a Hive
release it has not been verified against. Upgrade PyHive when the server is
newer; from the SDK, `skip_version_check=True` tries anyway.

## Docs and examples

The documentation and example scripts ship inside the package.

```bash
pyhive docs list                    # list the pages (also plain `pyhive docs`)
pyhive docs show sdk                # print a page as Markdown
pyhive docs path                    # where the files are
pyhive docs install-skill           # install them as the Claude Code skill `pyhive`
pyhive docs install-skill --project .   # ...into ./.claude/skills instead of ~/.claude/skills

pyhive examples list                # list the example scripts (also plain `pyhive examples`)
pyhive examples show program_tree   # print one
pyhive examples run program_tree 2  # run one against the server
```

`examples run` signs in exactly like every other command and passes any extra
arguments to the example. Its output is the example's own text, not JSON.
`python -m pyhive.examples` is the same command group.
