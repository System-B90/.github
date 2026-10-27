# Examples

Runnable scripts ship inside the package. Each one is a short, complete
program you can copy as a starting point.

```bash
pyhive examples                          # list them
pyhive examples show program_tree        # print one
pyhive examples run program_tree 2       # run one against the server
```

`pyhive examples run` signs in the same way as every other `pyhive` command
(see [Signing in](cli.md#signing-in)) and passes extra arguments on to the
example. Run as a plain script (`python program_tree.py`), an example signs in
through the browser instead.

Every example defines `main(client, *args)`, so you can also call one from
your own code or a notebook:

```python
from pyhive import examples
examples.load("program_tree").main(client, "2")
```

| Example | What it does |
| ------- | ------------ |
| [`connect`](#connect) | Every way to sign in to Hive, then print the server version and what you can see. |
| [`program_tree`](#program_tree) | Print the course tree — program, subjects, modules, exercises — with counts. |
| [`find_student`](#find_student) | Find a student by name or number and show their mentor, classes and progress. |
| [`assignments_csv`](#assignments_csv) | Export assignments as CSV — student, subject, module, exercise, status, submissions. |
| [`class_roster`](#class_roster) | Print every class (rooms and student groups) with its members. |
| [`weekly_schedule`](#weekly_schedule) | Print the schedule for the next seven days, grouped by day. |
| [`open_help_requests`](#open_help_requests) | List open help requests: who asked, about which exercise, and when it was last answered. |
| [`build_module`](#build_module) | Create a subject, a module and its exercises from a plain Python outline. |

The source of each example is below. (Reading this file raw, as an agent
does, the source appears as a `--8<--` include line: print it with
`pyhive examples show NAME`.)

## connect

```python
--8<-- "pyhive/examples/connect.py"
```

## program_tree

```python
--8<-- "pyhive/examples/program_tree.py"
```

## find_student

```python
--8<-- "pyhive/examples/find_student.py"
```

## assignments_csv

```python
--8<-- "pyhive/examples/assignments_csv.py"
```

## class_roster

```python
--8<-- "pyhive/examples/class_roster.py"
```

## weekly_schedule

```python
--8<-- "pyhive/examples/weekly_schedule.py"
```

## open_help_requests

```python
--8<-- "pyhive/examples/open_help_requests.py"
```

## build_module

```python
--8<-- "pyhive/examples/build_module.py"
```
