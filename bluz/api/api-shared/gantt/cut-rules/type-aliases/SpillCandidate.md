[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / SpillCandidate

# Type Alias: SpillCandidate

> **SpillCandidate** = `object`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:107](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-rules.ts#L107)

Whether an occurrence may be moved off the day it was mapped to.

Pinned in place:
- **Meal events** — their whole purpose is a fixed clock time.
- **Everything belonging to a daily recurrence**, echo *and* anchor alike.
  "Every day" stops being true the moment one occurrence hops, and moving
  the anchor is worse than moving an echo: the echo days were derived from
  the anchor's mapping before balancing ran, so relocating it leaves the
  mapped day empty and doubles up on the day it landed on.

Free to move: ordinary mapped events and **weekly** recurrences — anchor and
echoes alike, each on its own merits, since a weekly event's day is a
preference rather than a promise.

## Properties

### isDailyRecurrence

> **isDailyRecurrence**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:113](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-rules.ts#L113)

True when the source event recurs daily.

***

### isPinnedMeal

> **isPinnedMeal**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:109](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-rules.ts#L109)

True for the auto-seeded meal events pinned to a clock time.

***

### isRecurrenceEcho

> **isRecurrenceEcho**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:111](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-rules.ts#L111)

True when this occurrence is a recurrence echo rather than the mapped day.
