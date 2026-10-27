# Week-Building Rules

Formal rules for `/bluz`. Each rule has an ID. Cite IDs in proposals.
Times are Israel local time. "Day" = one calendar date in the week.

Glossary:

- **Shuffle** — group of students. Per syllabus, each student is in exactly 1 shuffle (שאפל).
- **Course tree** — Bis90 → at most one of Apollo / Mivtzar / Sphinx / Hermon → sub-courses.
- **Block** — maximal run of consecutive events between two breaks/prayers/meals.
- **Event types** (`ModuleEventType`): `הרצאה` lecture, `ע"ע` exercise,
  `ל"ע` self-teaching, `אחר` other.
- **כללי** — the general syllabus.
- **מרוחקים** — students living far away.
- **סגירת שבת** — `weekendDuty`, students stay at school on Friday & Saturdayץ

---

## §0. Priority Tiers

When rules conflict, the higher tier wins. Within a tier, lower ID wins.

| Tier | Name           | Rules                                                                                                                                                     |
| ---- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H    | Hard frames    | §1, §2, §2.1 (Thursday), §3, R-40 (meals), R-71 (fixed rooms), §4.2 (א"ג), R-46 (מתואם), R-47 (Gantt order), R-60 (one event per room), R-68 (instructor) |
| A    | Alignment      | §5                                                                                                                                                        |
| S    | Soft placement | rest of §4, R-61..R-65, R-69, §7                                                                                                                          |
| B    | Breaks         | `cut-rules.ts` `BREAK_RULES` order                                                                                                                        |
| C    | Constraints    | §8 — all soft, fixed last                                                                                                                                 |

- **R-01** Tier H is never violated without explicit user approval.
- **R-02** Prefer overlap over placing outside a day's window (`CUT_PRIORITY_LADDER`).
- **R-03** Events stay in their week. Moves inside the week are allowed, moves out of the week are a last resort and require explicit user approval.

---

## §1. Sunday Arrival

- **R-10** Sunday 08:00–10:00 holds one block `הגעה מהבית`. Nothing else.
- **R-11** All students must be in by 10:00. מרוחקים by 11:00.
- **R-12** Sunday 10:00–11:00 holds **only** `ע"ע` events from the `כללי`
  syllabus ("ע"ע כ'"). Nothing a מרוחק student would miss.
- **R-13** No `ע"ע כ'` available → leave 10:00–11:00 empty. Never fill it with
  other content.
- **R-14** Sunday after a `weekendDuty` week: **no** `הגעה מהבית`, R-11/R-12 do
  not apply. Day starts at its normal start time.

## §2. Friday Exit (normal week)

- **R-20** Week without `weekendDuty`: Friday work time ends at **08:30**
  (`יציאה הביתה`). That window holds **only `ע"ע כ'`** (`ע"ע` from `כללי`),
  about 1 hour. No other event type or syllabus. Nothing after 08:30.
  The `ע"ע כ'` hour goes after breakfast, or is split around it (part before,
  part after). Breakfast time comes from the iteration's `mealTimes` (R-45).
- **R-21** מרוחקים leave the base at **07:00**. Nothing on Friday may be
  something they must attend.
- **R-22** Any other content mapped to Friday moves **earlier** in the same
  week (an explicit exception to the cut's forward-only spill).
- **R-23** No `משוב יומי` on Fridays.
- **R-24** Week without `weekendDuty`: Saturday holds **nothing**. Any event
  there moves earlier in the week (R-22).

## §2.1 Thursday Morning

- **R-25** Every Thursday, in this order, nothing else between them:
    1. Breakfast (time from `mealTimes`, R-45).
    2. `הכנות למסדר מגורים` — from breakfast end until 08:30.
    3. `מסדר מגורים` at **08:30**, until 09:00.
    4. `מסדר הנפה` at **09:00**.
- **R-26** No other event starts before `מסדר הנפה` ends. Its end is the
  calendar event's `endTime`. Missing event → ask; don't guess its length.
- **R-27** These events are fixed frames, like meals. Don't create them
  unless the user asks; missing one → report it under **Problems**.

## §3. weekendDuty Weeks & Shabbat

- **R-30** `weekendDuty = true`: no early Friday exit. Friday is a working day.
- **R-31** Only when `weekendDuty = true`, Saturday may hold any event that fits after havdalah (R-32).
- **R-32** Shabbat window from the server (`bluz shabbat`), location **Beer Sheva**:
    - Friday: last event ends **≥ 2h before** candle lighting (`כניסת שבת`).
    - Saturday: first event starts **≥ 30 min after** havdalah (`צאת שבת`).
    - Nothing inside `[candle lighting − 2h, havdalah + 30m]`.

Computing it: ask the server, don't compute locally.

```
bluz --json shabbat <any-date-in-the-week>
```

Returns `candleLighting` (כניסת שבת), `havdalah` (צאת שבת),
`fridayLastEventEnd` (candle lighting − 2h) and `saturdayFirstEventStart`
(havdalah + 30m), Israel local `HH:mm`, for that Sunday-to-Saturday week.
Use those bounds directly. One request; no code to run.

## §4. Event-Type Placement

- **R-40** Meals are fixed. Never move them (see "Scheduling guardrails" in [cli-reference.md](cli-reference.md)).
- **R-41** No `הרצאה` during the `שחרית` window (from schedule prayer settings).
- **R-42** Lectures avoid other prayer windows best-effort
  (`PRAYER_RULES.avoidOverlapForTypes`).
- **R-43** Lectures after lunch are fine — there are too many lectures to
  avoid it. Other lecture-time preferences: ask at runtime only if relevant.
- **R-44** Daily-recurring events keep their day and time (pinned).
- **R-45** Day bounds, meal times and prayer times come from the **iteration
  settings**: `bluz --json iterations settings <iteration-id>` returns
  `schedule` (day start / weekend-home start / calendar bounds), `mealTimes`
  and `prayerTimes`. Read them; never assume defaults.
- **R-46** **מתואם events don't move.** Only a calendar event with
  `locked: true` (UI: מתואם) is pinned: same day, same time, same room. Plan around it
  like a meal. The Gantt has no such data — Gantt `isCritical` does **not**
  pin an event.
- **R-47** **Gantt order is binding.** Within a module, events keep their Gantt
  order. Within a syllabus, modules keep their Gantt order. Reorder across
  syllabuses freely; never within one.
- **R-48** No per-day load limit. A day may hold 14 hours of one syllabus. Daily limit is the working hours available from the gantt curriculum weeks.

### §4.1 משוב יומי

- **R-49a** Use the `משוב יומי` events that exist in the Gantt. Don't create
  them. Usually 10 min.
- **R-49b** It goes **after all regular events** of the day. A **special**
  event may come after it. Special = any of:
    - a very long `סדנה` (workshop);
    - an event with specific notes/comments;
    - a מתואם event (R-46) which states it must be at night;
    - `א"ג` placed as the day's last event (§4.2).
- **R-49e** The agent doesn't decide "special" alone. For **each** event that
  _might_ be special, ask the user (`AskUserQuestion`):
    1. Is it special? yes / no.
    2. If yes — should it go **after** `משוב יומי`? yes / no.
       Batch up to 4 events per question call. Use the answers as given.
- **R-49c** If it can't fit that evening, move it to the **next morning**
  (still before regular content that day).
- **R-49d** Never on Friday, unless it was moved from Thursday to the morning (R-23).

### §4.2 א"ג and its התארגנות

- **R-48a** `התארגנות לפני א"ג` sits **immediately before** `א"ג`;
  `התארגנות אחרי א"ג` **immediately after** it. No gap, no event between.
  Move them together with the `א"ג`.
- **R-48b** Either may be omitted when:
    - `א"ג` is the day's last event (then it comes **after** `משוב יומי`,
      R-49b) — omit `התארגנות אחרי א"ג`;
    - `א"ג` directly follows a break of **> 20 min** — omit
      `התארגנות לפני א"ג`;
    - `א"ג` is directly followed by a break of **> 20 min** — omit
      `התארגנות אחרי א"ג`.
- **R-48c** Omitting one = leaving it out of the draft. List each omission
  (which, why) under **Issues** in the proposal; never delete silently.

## §5. Shuffle Alignment

- **R-50** All shuffles of one syllabus share **block edges**: every block
  starts and ends at the same times across those shuffles. Events inside a
  block may differ.
- **R-51** Daily syllabus minutes are identical across its shuffles, not
  across courses.
- **R-52** Events tied to some **courses** (not shuffles) need not align with
  other courses' events.
- **R-53** Syllabuses of mutually exclusive courses don't constrain each other.
- **R-54** Breaks of no more than 15 minutes may be added for specific shuffles if needed for alignment.

### §5.3 Splitting

- **R-55** Only events with `splitAcrossBreaks = true` may be split.
- **R-56** Split to make R-50 hold, or to fit around a meal/prayer. Never for
  convenience.
- **R-57** Each piece ≥ **30 min**. Down to **20 min** only when no other
  arrangement exists; say so in the proposal. Under 20 min → never; ask.
- **R-58** Pieces keep title, type, syllabus, shuffles. Total minutes unchanged. Lecturer unchanged, instructor may change.
- **R-59** Prefer fewer splits. Prefer the split point on the break itself.
- **R-5A** Pieces may land on different days of the week (e.g. Monday and
  Wednesday), and other syllabuses' events may sit between them. Order
  across pieces still follows R-47.

## §6. Rooms

- **R-60** One event per room at a time. Hard.
- **R-61** Capacity field depends on event type:
    - `הרצאה` → `lectureSeatCount` ≥ attendees.
    - `ע"ע`, `ל"ע`, `סדנה` (workshop) → `workstationCount` ≥ attendees.
    - Field is `null` → room unusable for that type unless the user says otherwise.
- **R-62** Pick the smallest room that fits. Lectures for many shuffles → big rooms.
- **R-63** Shuffle/course headcount unknown → `AskUserQuestion`. Don't guess.
- **R-64** Room changes between consecutive events of the same students →
  **5 min** transition (`מעבר כיתה`). Not for `ללא כיתה` / `בחוץ`.
- **R-65** Prefer keeping a shuffle in one room across a block (fewer R-64 gaps).
- **R-66** Ignore room reservations for now.
- **R-70** Default rooms always exist: `רחבת מסדרים`, `מגורים`, `חדר אוכל`.
  Check `bluz --json rooms list` at the start. Missing → ask the user
  (`AskUserQuestion`) before creating it. Only on yes: create it as a custom
  room (`bluz rooms create --name "..."`). On no: report it under **Problems**.
- **R-71** Fixed room per event, always (overrides R-61..R-65):
    - All meal breaks → `חדר אוכל`.
    - `התארגנות לפני א"ג`, `התארגנות אחרי א"ג` (if present), `מסדר מגורים`, `הכנות למסדר מגורים` → `מגורים`.
    - `מסדר הנפה`, `הגעה מהבית`, `יציאה הביתה`, `א"ג` → `רחבת מסדרים`.
      Other events never use these rooms.

## §6.1 Instructors

- **R-67** At the start of the run, ask whether to also allocate instructors (מבזרים) & lecturers (מרצים).
  No → skip §6.1.
- **R-68** An instructor teaches **one shuffle (or one course) at a time**. Hard
  when allocating.
- **R-69** An instructor may also be the lecturer of an event. Allowed, not
  recommended — prefer someone else when possible.
- **R-6A** Prefer instructors who are **members of the event's course**. Fall
  back to others only when no member is free; flag it in the proposal.
  Membership = the course's `instructorIds` (Hive ids), set in the Course
  Builder (`בניית מסלולים`), stored in MongoDB `courses`. Read with
  `bluz --json courses list`.

## §7. Breaks

- Strive for cumulative 45 min of breaks per day excluding meals.
- 15 min after ≥ 90 min continuous `ע"ע`.
- 10–15 min between different syllabuses.
- 10 min after ≥ 45 min lecture/`ע"ע` run.
- Breaks cover prayers when possible.
- No generated break adjacent to a meal.
- Breaks never extend a day.

## §8. Constraint Pass

Runs **after** the draft is built, before the proposal.

- **R-80** Load the curriculum's `GanttConstraint`s
  (`bluz --json gantt curriculums constraints <curriculum-id>`): after/before
  with min/max day delays, allowed/forbidden weekdays.
- **R-81** **All constraints are SOFT.** Never block the week on one.
- **R-82** For each violated constraint, try to fix it by moves inside the week
  that break **no** tier-H or tier-A rule. Prefer the smallest move.
- **R-83** A fix that would break a higher-tier rule → don't apply. List the
  constraint under **Violations** with the reason.
- **R-84** After any fix, re-check every rule (fixes can cascade). Repeat until
  stable or **3 passes** max, then stop and report what's left.
- **R-85** Report every constraint: satisfied / fixed (how) / left violated (why).

---

## Open Questions

Answer → move into the rules with an ID.

None right now. New unwritten rule found during a run → ask the user, then add
it here or straight into the rules.
