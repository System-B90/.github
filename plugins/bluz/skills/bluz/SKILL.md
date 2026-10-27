---
name: bluz
description: Drive the Bluz scheduling/curriculum app via the `bluz` CLI, and build a week's schedule ("/bluz Build the schedule for week 5"). Use for any request to read/write Bluz data — rooms, courses, outsiders, reservations, iterations, calendar events, drafts/snapshots, gantt curriculum tree, the cut pipeline, settings, colors, Hive reference data, Google Calendar — or to organize a week (shuffle alignment, rooms, splits, Sunday arrival, Friday exit, weekendDuty/Shabbat, משוב יומי). Replaces the deprecated `bluz-cli` skill.
argument-hint: Build the schedule for week <N> | <any Bluz request>
---

# /bluz

One entry point for everything Bluz. Pick the task, read only its files.

| Request                                                          | Read                                                                      |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Build / organize / fix a week ("Build the schedule for week 5")  | [week-builder.md](week-builder.md) then [RULES.md](RULES.md) — both fully |
| Anything else: read or write Bluz data, the cut, settings, Gantt | [cli-reference.md](cli-reference.md)                                      |

Week building also uses `cli-reference.md` for exact command syntax.

## Always

- Use `bluz --json …` for anything you parse.
- Pass `--yes` to delete/cancel commands, or they block on a prompt.
- Meal breaks are fixed. Never move them unless the user names the break.
- Snapshot before bulk writes (see `cli-reference.md` → Quick recipes).
- `bluz` missing? The plugin's SessionStart hook installs it; otherwise run
  the install lines in `cli-reference.md` → Setup.
