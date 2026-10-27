# Python SDK

`pyhive` is a synchronous Python client for the Hive LMS API. One object,
`HiveClient`, signs in and exposes every resource as methods. Results come
back as typed Pydantic models with helpers for walking between related
objects.

```python
from pyhive import HiveClient

with HiveClient.from_sso("https://hive.org") as client:
    for program in client.get_programs():
        for subject in program.get_subjects():
            print(program.name, subject.symbol, subject.name)
```

## Install

```bash
pip install PyHiveLMS --index-url https://system-b90.github.io/.github/pypi/
```

To skip `--index-url` from now on:
`pip config set global.extra-index-url https://system-b90.github.io/.github/pypi/`.
In a `requirements.txt`, put
`--extra-index-url https://system-b90.github.io/.github/pypi/` above `PyHiveLMS`.
Python 3.10 or newer.

## Connecting

```python
from pyhive import HiveClient

# Browser sign-in (SSO). The token refreshes itself.
client = HiveClient.from_sso("https://hive.org")

# Username and password. The token refreshes itself.
client = HiveClient("username", "password", "https://hive.org")

# An access token you already have (e.g. from `pyhive token`).
# It cannot refresh: when it expires, create a new client.
client = HiveClient.from_api_token(token, "https://hive.org")

# An access token plus its refresh token: refreshes itself.
client = HiveClient.from_api_token(
    token, "https://hive.org", refresh_token=refresh, auth_strategy="sso"
)

# Whatever the `pyhive` CLI would use: the server and sign-in cached by
# `pyhive auth login`, or -u/-p, HIVE_ACCESS_TOKEN, then SSO.
from pyhive.cli.client_factory import default_hive_url, get_hive_client
client = get_hive_client(default_hive_url(), verify=False)
```

Use the client as a context manager (`with ... as client:`) to close its HTTP
connection when you are done.

Every constructor also takes:

| Keyword              | Default | Meaning                                                                 |
| -------------------- | ------- | ----------------------------------------------------------------------- |
| `verify`             | `True`  | Verify TLS. Pass `False` for a server with a self-signed certificate.   |
| `timeout`            | httpx's | Seconds (float) or an `httpx.Timeout`.                                  |
| `skip_version_check` | `False` | Don't check the server's Hive version on connect (see [Versions](#versions)). |
| `headers`, `proxy`   |         | Passed to the underlying `httpx.Client`.                                |

Requests that get HTTP 502 are retried with backoff (up to 5 tries). A 401
triggers one token refresh and a retry, when the sign-in method can refresh.

## Reading data

### Lists are generators

Every `get_<things>()` method returns a generator that pages through Hive as
you iterate. Wrap it in `list()` to count, index or iterate twice.

```python
subjects = list(client.get_subjects())
print(len(subjects), subjects[0].name)
```

### Filters

List methods take keyword filters named after Hive's query parameters. Pass
either ids or model objects wherever a related object is expected:

```python
client.get_subjects(parent_program=program)            # or parent_program=2
client.get_modules(parent_subject__id=12)
client.get_exercises(parent_module=module)
client.get_assignments(for_user=student)               # or for_user=13
client.get_assignments(for_mentees_of=mentor, parent_subject=subject)
client.get_users(classes__id__in=[3, 4], clearance__in=[ClearanceEnum.HANICH])
client.get_classes(type_=ClassTypeEnum.ROOM)
client.get_help_requests(help_status__in=["Open"], ordering="-id")
```

- `subject_name=`, `module_name=`, `exercise_name=`, `program_name=` match the
  name **exactly**.
- Filters that contradict each other (`for_user=` and a different
  `user__id__in=`) raise `AssertionError`.

### One object

```python
program = client.get_program(2)
subject = client.get_subject(12)
module = subject.get_module("Loops")      # by exact name; ValueError if 0 or 2+ match
exercise = module.get_exercise("For loops")
student = client.get_student(number=1234) # or name="First Last"
```

`get_student` returns `None` when no single student matches.
`get_user_by_name(name, clearance=...)` does the same lookup for any user.

### Related objects

Models load related objects on first access and cache them:

```python
assignment = client.get_assignment(1234)
assignment.user.display_name         # one request
assignment.exercise.parent_module    # one request each
student.mentor, student.classes, student.program
```

Each first access is a request. Inside a loop over hundreds of objects, fetch
the related table once and join by id instead:

```python
users = {user.id: user for user in client.get_users()}
for assignment in client.get_assignments():
    print(users[assignment.user_id].display_name, assignment.assignment_status.value)
```

## Models

Models live in `pyhive.types` and are Pydantic V2 models:

```python
from pyhive.types import Assignment, AssignmentStatusEnum, ClearanceEnum, Subject, User
```

- Fields use Python names: related objects are ids named `<thing>_id` or
  `<thing>_ids` (`user.mentor_id`, `user.class_ids`, `module.parent_subject_id`).
- `model.to_dict()` gives Hive's wire format (`{"mentor": 1, "classes": [...]}`),
  the same shape `pyhive --json` prints.
- Enum fields hold enum members. Compare with members:
  `assignment.assignment_status == AssignmentStatusEnum.DONE`; use `.value` for
  the display string.

| Model        | Helpers                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------ |
| `Program`    | `get_subjects()`, `create_subject(...)`, `delete()`, `.checker`, `.default_class`                |
| `Subject`    | `get_modules()`, `get_module(name)`, `create_module(...)`, `delete()`, `.parent_program`         |
| `Module`     | `get_exercises()`, `get_exercise(name)`, `create_exercise(...)`, `delete()`, `.parent_subject`   |
| `Exercise`   | `get_assignments()`, `delete()`, `.parent_module`, `.parent_subject`                             |
| `Assignment` | `get_responses()`, `.user`, `.checker`, `.exercise`                                              |
| `AssignmentResponse` | `iter_contents()`, `.user`, `.assignment`                                                |
| `User`       | `get_assignments()`, `update()`, `set_queue(q)`, `delete()`, `.mentor`, `.mentees`, `.classes`, `.program`, `.queue`, `.current_assignment` |
| `Class`      | `update()`, `delete()`, `.users`, `.program`                                                     |
| `Lesson`     | `get_rules()`, `.module`                                                                         |
| `Queue`      | `delete()`, `.user`, `.module`, `.subject`, `.program`                                           |
| `Help`       | `delete()`, `.user`, `.checker`, `.for_exercise`                                                 |

Common enums: `ClearanceEnum` (`HANICH` = student, `CHECKER`, `SEGEL` = staff,
`ADMIN`), `AssignmentStatusEnum` (`NEW`, `WORK_IN_PROGRESS`, `REDO`,
`SUBMITTED`, `AUTOCHECKED`, `DONE`), `StatusEnum` (where a student is:
`PRESENT`, `TOILET`, `HOME`, …), `GenderEnum`, `ClassTypeEnum` (`ROOM`,
`STUDENT_GROUP`), `HelpTypeEnum`, `HelpStatusEnum`, `VisibilityEnum`.

## Creating and changing data

### Course content

```python
program = client.get_program(2)
subject = program.create_subject(symbol="PY", name="Python", color="#3F51B5")
module = subject.create_module(name="Basics", order=1)
exercise = module.create_exercise(name="Loops", order=1, expected_duration="45:00")

subject.delete()     # also deletes its modules and exercises
```

The same calls exist on the client: `client.create_subject(symbol, name,
program, color)`, `client.create_module(name, parent_subject, order)`,
`client.create_exercise(name, order, parent_module, ...)`.

### Users and classes

```python
from pyhive.types import ClassTypeEnum, ClearanceEnum, GenderEnum, StatusEnum

student = client.create_student(
    "jdoe", "S3cret!", GenderEnum.FEMALE, number=1234, program=2,
    first_name="Jane", last_name="Doe", mentor=mentor,
)
staff = client.create_user(
    "mentor1", "S3cret!", clearance=ClearanceEnum.SEGEL, gender=GenderEnum.MALE
)

student.status = StatusEnum.HOME     # change fields locally...
student.update()                     # ...then save them

group = client.create_class(
    "Group A", program=2, users=[student], type_=ClassTypeEnum.STUDENT_GROUP
)
client.get_students(of_class=group)  # also of_mentor=, of_program=
```

### Assignments

```python
client.patch_assignment(assignment, description="Look at line 12")
client.lock_assignment(assignment)       # the student can no longer submit
client.unlock_assignment(assignment)
for response in assignment.get_responses():
    print(response.date, response.response_type, response.dear_student)
```

### Schedule

```python
from datetime import datetime, timedelta, timezone

start = datetime(2026, 11, 1, 8, 0, tzinfo=timezone.utc)
event = client.create_schedule_event(start, start + timedelta(hours=2), title="Lecture")
client.create_event_attendee(event, attendee_class=3)    # a class attends
client.create_event_instructor(event, instructor=1)      # a user teaches

week = client.get_schedule_events(start__gte=start, end__lte=start + timedelta(days=7))
client.delete_schedule_event(event)
```

Newer Hive releases identify lessons, events, event categories, tags and
their links by UUID instead of an integer. Methods that take one accept a
`UUID`, its string form, an `int`, or the model itself.

### Help requests

```python
chat = client.create_chat(with_user=student, title="Checking in")
for response in client.get_help_responses(chat):
    print(response.date, response.response_type)
chat.delete()
```

A staff account can open only chats. `create_help_request` with another
`HelpTypeEnum` is for student accounts.

## Errors

| Situation                                  | Exception                                                                      |
| ------------------------------------------ | ------------------------------------------------------------------------------ |
| Hive rejects a create (HTTP 400)            | `ValueError("HTTP 400 Error: {...}")`, carrying Hive's validation message     |
| Not found, forbidden, other HTTP errors     | `httpx.HTTPStatusError` (`exc.response.status_code`)                           |
| A delete Hive did not confirm               | `RuntimeError("Failed to delete!")`                                            |
| Bare token expired (`from_api_token` without refresh) | `RuntimeError`: sign in again and create a new client               |
| Server runs a Hive release PyHive has not verified | `UnverifiedHiveVersionError` (a `RuntimeError`)                          |
| PyHive refuses the arguments               | `ValueError` / `AssertionError` with the reason                                |

```python
import httpx

try:
    client.get_program(999)
except httpx.HTTPStatusError as exc:
    if exc.response.status_code == 404:
        print("no such program")
```

## Versions

When it connects, the client asks the server for its Hive version and checks
it against the exact releases this PyHive is verified against (`pyhive
versions` lists them). An unlisted release raises `UnverifiedHiveVersionError`:
upgrade PyHive, or pass `skip_version_check=True` to try anyway.

```python
client.get_hive_version()     # e.g. "7.2.0"
```

## Method reference

Every public `HiveClient` method. "Id or model" arguments accept either.

### Connection and server

| Method                                                    | Does                                                         |
| --------------------------------------------------------- | ------------------------------------------------------------ |
| `HiveClient(username, password, hive_url, ...)`           | Sign in with a password                                      |
| `HiveClient.from_sso(hive_url, ...)`                      | Sign in through the browser                                  |
| `HiveClient.from_api_token(api_token, hive_url, ...)`     | Use an existing token                                        |
| `get_hive_version()`                                      | The server's Hive version                                    |
| `get_server_time()`                                       | The server's clock                                           |
| `get_powersync_token()`                                   | A PowerSync sync token                                       |
| `get_client_info(client_id)`                              | Public metadata of an SSO client                             |
| `register_sso_service(service_name, redirect_uris)`       | Register an SSO client app; returns its id and secret        |
| `get(endpoint)`, `post(endpoint, data)`, `put(...)`, `patch(...)`, `delete(endpoint)` | Raw JSON requests to any Hive endpoint |
| `post_empty(endpoint)`, `put_empty(endpoint)`             | Raw request with an empty body                               |

### Programs, subjects, modules, exercises

| Method                                                     | Does                                                    |
| ---------------------------------------------------------- | ------------------------------------------------------- |
| `get_programs(id__in=, program_name=)`                     | List programs                                           |
| `get_program(program_id)`                                  | One program                                             |
| `create_program(name, checker=, ...)`                      | Create a program                                        |
| `delete_program(program)`                                  | Delete a program                                        |
| `get_subjects(parent_program=, subject_name=, ...)`        | List subjects                                           |
| `get_subject(subject_id)`                                  | One subject                                             |
| `create_subject(symbol, name, program, color, segel_brief=)` | Create a subject                                      |
| `delete_subject(subject)`                                  | Delete a subject with its modules and exercises         |
| `get_modules(parent_subject=, parent_program=, module_name=, ...)` | List modules                                    |
| `get_module(module_id)`                                    | One module                                              |
| `create_module(name, parent_subject, order, segel_brief=)` | Create a module                                         |
| `delete_module(module)`                                    | Delete a module                                         |
| `create_daily_review(date, show_lesson_names=)`            | Generate the Daily Review module for a date             |
| `get_exercises(parent_module=, parent_subject=, exercise_name=, ...)` | List exercises                               |
| `get_exercise(exercise_id)`                                | One exercise                                            |
| `create_exercise(name, order, parent_module, ...)`         | Create an exercise                                      |
| `delete_exercise(exercise)`                                | Delete an exercise                                      |
| `get_exercise_fields(exercise)`                            | The form fields of an exercise                          |
| `get_exercise_field(exercise, field_id)`                   | One form field                                          |

### Assignments

| Method                                                    | Does                                                          |
| --------------------------------------------------------- | ------------------------------------------------------------- |
| `get_assignments(for_user=, for_mentees_of=, parent_module=, parent_subject=, ...)` | List assignments                    |
| `get_assignment(assignment_id)`                           | One assignment                                                |
| `patch_assignment(assignment, **fields)`                  | Change some fields                                            |
| `update_assignment(assignment)`                           | Save a locally changed assignment                             |
| `delete_assignment(assignment)`                           | Delete an assignment                                          |
| `lock_assignment(assignment)`, `unlock_assignment(assignment)` | Stop / allow the student submitting                      |
| `subscribe_to_assignment(assignment)`, `unsubscribe_from_assignment(assignment)` | Notifications for the current user |
| `get_assignment_responses(assignment)`                    | The submissions and checks on an assignment                   |
| `get_assignment_response(assignment, response_id)`        | One response                                                  |
| `get_latest_assignments(...)`                             | Up to 100 recently submitted assignments (staff feed)         |
| `create_latest_assignment(**fields)`, `update_latest_assignment(latest_id, **fields)`, `delete_latest_assignment(latest_id)` | Manage that feed |

### Users, classes, seating, queues

| Method                                                    | Does                                                          |
| --------------------------------------------------------- | ------------------------------------------------------------- |
| `get_users(classes__id__in=, clearance__in=, mentor__id=, program__id__in=, ...)` | List users                             |
| `get_user(user_id)`                                       | One user                                                      |
| `get_user_me()`                                           | Not implemented: raises `NotImplementedError`                 |
| `get_user_by_name(name, clearance=)`                      | One user by full name, display name, username or first name   |
| `get_students(of_mentor=, of_class=, of_program=)`        | List students                                                 |
| `get_student(name=, number=)`                             | One student by name and/or number, or `None`                  |
| `create_user(username, password, clearance=, gender=, ...)` | Create a user                                               |
| `create_student(username, password, gender, number=, program=, ...)` | Create a student                                   |
| `update_user(user)`                                       | Save a locally changed user (same as `user.update()`)         |
| `delete_user(user)`                                       | Delete a user                                                 |
| `set_users_queue(user, queue)`                            | Put a user on a queue                                         |
| `get_classes(id__in=, name=, program__id__in=, type_=)`   | List classes                                                  |
| `get_class(class_id)`                                     | One class                                                     |
| `create_class(name, program=, users=, type_=, ...)`       | Create a class                                                |
| `update_class(class_, users_from_classes=)`               | Save a locally changed class                                  |
| `delete_class(class_)`                                    | Delete a class                                                |
| `import_users_to_class(to_class, from_classes)`           | Add every member of other classes to a class                  |
| `get_seatings(classroom__id=)`, `get_seating(seating_id)` | Seats in rooms                                                |
| `create_seating(classroom, x, y, hostname=, hanich=)`     | Add a seat                                                    |
| `update_seating(seating, **fields)`, `delete_seating(seating_id)` | Change / remove a seat                                |
| `get_queue(queue_id)`                                     | One queue                                                     |
| `create_queue(name, description=, module=, user=)`, `delete_queue(queue)` | Create / delete a queue                       |

### Help requests and notifications

| Method                                                    | Does                                                          |
| --------------------------------------------------------- | ------------------------------------------------------------- |
| `get_help_requests(help_status__in=, help_type__in=, user__id__in=, ordering=, ...)` | List help requests and chats        |
| `get_help_request(help_id)`                               | One help request                                              |
| `create_help_request(user, title, type_, exercise, visibility)` | Open a help request (student accounts)                  |
| `create_chat(with_user=, title=, about_exercise=, visibility=)` | Open a chat with a user                                 |
| `delete_help_request(help_request)`, `delete_chat(chat)`  | Delete one                                                    |
| `get_help_responses(help)`, `get_help_response(help, response_id)` | Replies on a help request                            |
| `get_help_response_student_file(help, response_id)`       | The file attached to a reply, as bytes, or `None`             |
| `get_notifications(was_read=, assignment=, help=, ...)`   | List notifications                                            |
| `get_notification(notification_id)`                       | One notification                                              |
| `create_notification(user, help=, assignment=, comment=)` | Create a notification                                         |
| `update_notification(notification, was_read=)`            | Mark read / unread                                            |
| `delete_notification(notification_id)`                   | Delete a notification                                         |

### Schedule and lessons

| Method                                                    | Does                                                          |
| --------------------------------------------------------- | ------------------------------------------------------------- |
| `get_schedule_events(start__gte=, end__lte=, lesson__id=)` | Events in a time window                                      |
| `get_schedule_event(event_id)`                            | One event                                                     |
| `create_schedule_event(start, end, title=, category=, room=, lesson=, ...)` | Create an event                             |
| `delete_schedule_event(event_id)`                         | Delete an event                                               |
| `get_event_categories()`, `get_event_category(id)`        | Event categories                                              |
| `create_event_category(name, color, ...)`, `update_event_category(category, **fields)`, `delete_event_category(id)` | Manage categories |
| `get_event_tags()`, `get_event_tag(id)`                   | Event tags                                                    |
| `create_event_tag(name, color)`, `update_event_tag(id, name=, color=)`, `delete_event_tag(id)` | Manage event tags        |
| `get_event_taggings()`, `create_event_tagging(event, tag)`, `delete_event_tagging(id)` | Tags on events                   |
| `get_event_attendees()`, `create_event_attendee(event, attendee_class)`, `delete_event_attendee(id)` | Classes attending events |
| `get_event_instructors()`, `create_event_instructor(event, instructor)`, `delete_event_instructor(id)` | Users teaching events  |
| `get_lessons(module=)`, `get_lesson(lesson_id)`           | Lessons                                                       |
| `create_lesson(name, module, description=)`, `update_lesson(lesson, **fields)`, `delete_lesson(lesson_id)` | Manage lessons |
| `get_lesson_rules(lesson=)`                               | A lesson's queue rules                                        |
| `create_lesson_rule(lesson=, ...)`, `update_lesson_rule(lesson=, rule_id=, **fields)`, `delete_lesson_rule(lesson=, rule_id=)` | Manage queue rules |

### Tags and SSO applications

| Method                                                    | Does                                                          |
| --------------------------------------------------------- | ------------------------------------------------------------- |
| `get_tags()`, `get_tag(tag_id)`                           | Exercise tags                                                 |
| `create_tag(name, color)`, `update_tag(tag, name=, color=)`, `delete_tag(tag_id)` | Manage tags                           |
| `get_sso_applications()`, `get_sso_application(application_id)` | Registered SSO applications                             |
| `create_sso_application(name, redirect_uris=, skip_authorization=)` | Register one                                        |
| `update_sso_application(application, **fields)`, `delete_sso_application(application_id)` | Change / remove one          |

Signatures and filters in full: `help(HiveClient.get_assignments)`, or
`inspect.signature(...)` in a script.
