[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanOptions

# Type Alias: CutPlanOptions

> **CutPlanOptions** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:342](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/gantt/cut-planner.ts#L342)

## Properties

### acceptedConstraintMoves?

> `optional` **acceptedConstraintMoves?**: `string`[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:366](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/gantt/cut-planner.ts#L366)

Constraint-solver moves the user accepted, by event id. Proposals not
listed here are reported but not applied — the cut never silently moves
an event the user mapped deliberately.

***

### autoSpillover?

> `optional` **autoSpillover?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:355](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/gantt/cut-planner.ts#L355)

Auto-spillover: rebalance each week so no day carries more than its
working window, cascading work forward within the week. Defaults to on —
pass `false` for the pre-#… raw stacking behaviour.

***

### force?

> `optional` **force?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:349](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/gantt/cut-planner.ts#L349)

When true, an unmapped event or an unsatisfied recurrence no longer
fails the whole plan — the offending event is dropped and planning
continues. Lets a user explicitly cut an unfinished gantt. A missing
start date is still fatal (nothing is datable without it).

***

### insertBreaks?

> `optional` **insertBreaks?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:360](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/gantt/cut-planner.ts#L360)

Break post-pass: spread a day's leftover slack through the day as real
הפסקה events instead of leaving it as an empty tail. Defaults to on.

***

### parkNonTemplate?

> `optional` **parkNonTemplate?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:385](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/gantt/cut-planner.ts#L385)

Place only what the week template places, and park everything else in
the schedule's unassigned box (ארגז) for the user to place by hand.
Meal events keep their fixed times. No breaks are spread, since the
gaps are where the parked work goes. Defaults to off: unpinned work is
auto-placed around the template's events.

***

### parkWeekOnly?

> `optional` **parkWeekOnly?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:377](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/gantt/cut-planner.ts#L377)

Park week-only mappings (#964) in the schedule's unassigned box instead
of auto-scheduling them, so the user places each one by hand. They take
no weekday time, so nothing else moves to make room for them.

***

### weekOverflowResolutions?

> `optional` **weekOverflowResolutions?**: `Record`\<`string`, [`WeekOverflowResolution`](../../cut-rules/type-aliases/WeekOverflowResolution.md)\>

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:371](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/gantt/cut-planner.ts#L371)

Per-week answer to a `week-overflow` decision. Absent weeks use
`OVERFLOW_RULES.defaultResolution` (`park`).
