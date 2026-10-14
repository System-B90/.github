[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanOptions

# Type Alias: CutPlanOptions

> **CutPlanOptions** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:317](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L317)

## Properties

### acceptedConstraintMoves?

> `optional` **acceptedConstraintMoves?**: `string`[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:341](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L341)

Constraint-solver moves the user accepted, by event id. Proposals not
listed here are reported but not applied — the cut never silently moves
an event the user mapped deliberately.

***

### autoSpillover?

> `optional` **autoSpillover?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:330](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L330)

Auto-spillover: rebalance each week so no day carries more than its
working window, cascading work forward within the week. Defaults to on —
pass `false` for the pre-#… raw stacking behaviour.

***

### force?

> `optional` **force?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:324](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L324)

When true, an unmapped event or an unsatisfied recurrence no longer
fails the whole plan — the offending event is dropped and planning
continues. Lets a user explicitly cut an unfinished gantt. A missing
start date is still fatal (nothing is datable without it).

***

### insertBreaks?

> `optional` **insertBreaks?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:335](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L335)

Break post-pass: spread a day's leftover slack through the day as real
הפסקה events instead of leaving it as an empty tail. Defaults to on.

***

### weekOverflowResolutions?

> `optional` **weekOverflowResolutions?**: `Record`\<`string`, [`WeekOverflowResolution`](../../cut-rules/type-aliases/WeekOverflowResolution.md)\>

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:346](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/gantt/cut-planner.ts#L346)

Per-week answer to a `week-overflow` decision. Absent weeks use
`OVERFLOW_RULES.defaultResolution` (`overlap-source`).
