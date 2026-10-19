[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanOptions

# Type Alias: CutPlanOptions

> **CutPlanOptions** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:339](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L339)

## Properties

### acceptedConstraintMoves?

> `optional` **acceptedConstraintMoves?**: `string`[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:363](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L363)

Constraint-solver moves the user accepted, by event id. Proposals not
listed here are reported but not applied — the cut never silently moves
an event the user mapped deliberately.

***

### autoSpillover?

> `optional` **autoSpillover?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:352](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L352)

Auto-spillover: rebalance each week so no day carries more than its
working window, cascading work forward within the week. Defaults to on —
pass `false` for the pre-#… raw stacking behaviour.

***

### force?

> `optional` **force?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:346](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L346)

When true, an unmapped event or an unsatisfied recurrence no longer
fails the whole plan — the offending event is dropped and planning
continues. Lets a user explicitly cut an unfinished gantt. A missing
start date is still fatal (nothing is datable without it).

***

### insertBreaks?

> `optional` **insertBreaks?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:357](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L357)

Break post-pass: spread a day's leftover slack through the day as real
הפסקה events instead of leaving it as an empty tail. Defaults to on.

***

### parkWeekOnly?

> `optional` **parkWeekOnly?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:374](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L374)

Park week-only mappings (#964) in the schedule's unassigned box instead
of auto-scheduling them, so the user places each one by hand. They take
no weekday time, so nothing else moves to make room for them.

***

### weekOverflowResolutions?

> `optional` **weekOverflowResolutions?**: `Record`\<`string`, [`WeekOverflowResolution`](../../cut-rules/type-aliases/WeekOverflowResolution.md)\>

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:368](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L368)

Per-week answer to a `week-overflow` decision. Absent weeks use
`OVERFLOW_RULES.defaultResolution` (`park`).
