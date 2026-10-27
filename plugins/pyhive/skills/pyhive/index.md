# PyHive

PyHive is the Python SDK and command-line tool for the
[Hive](https://hive.org) learning management system. It reads and changes
programs, subjects, modules, exercises, assignments, users, classes, the
schedule and help requests.

- **`pyhive`** — a CLI for quick reads and deletes, with `--json` output for
  scripts and agents. → [CLI reference](cli.md)
- **`from pyhive import HiveClient`** — a typed Python client for everything
  else. → [Python SDK](sdk.md)
- **Examples** — runnable scripts shipped in the package. → [Examples](examples.md)
- **Claude Code skill** — teaches an agent to use both. → [Agent skill](SKILL.md)

## Install

```bash
pip install PyHiveLMS --index-url https://system-b90.github.io/.github/pypi/
pyhive version
```

PyHive is published to the System-B90 package index, not to PyPI (whose
`PyHiveLMS` is an old release). Python 3.10 or newer.

## Try it

```bash
pyhive auth login                   # pick the server and sign in once through the browser
pyhive programs list
pyhive --json subjects list | jq '.subjects[].name'
pyhive examples run program_tree
```

```python
from pyhive import HiveClient

with HiveClient.from_sso("https://hive.org") as client:
    program = next(iter(client.get_programs()))
    for subject in program.get_subjects():
        modules = list(subject.get_modules())
        print(f"[{subject.symbol}] {subject.name}: {len(modules)} modules")
```

## For AI agents

The pages here double as a [Claude Code](https://claude.com/claude-code) skill
called `pyhive`. Install it one of two ways:

```bash
# From the installed package, into ~/.claude/skills/pyhive:
pyhive docs install-skill

# Or as a plugin, which also installs PyHive when it is missing:
claude plugin marketplace add System-B90/.github
claude plugin install pyhive@system-b90-marketplace
```

Without Claude Code, point an agent at `pyhive docs show skill`: it prints the
same guide.

## The docs in your terminal

Every page here ships inside the package:

```bash
pyhive docs                 # list the pages
pyhive docs show sdk        # print one as Markdown
```

The published site is built from those same files, so the site, the terminal
and the skill always match the installed version.

## Supported Hive versions

PyHive works with the exact Hive releases it has been verified against.
`pyhive versions` lists them. Connecting to any other release raises
`UnverifiedHiveVersionError`; upgrade PyHive, or see [Versions](sdk.md#versions).
