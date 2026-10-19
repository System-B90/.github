[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / PlannedOccurrence

# Type Alias: PlannedOccurrence

> **PlannedOccurrence** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:192](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L192)

## Properties

### endTime

> **endTime**: `Date`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:197](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L197)

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:193](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L193)

***

### generatedBreak?

> `optional` **generatedBreak?**: `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:218](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L218)

Set on occurrences the break post-pass generated rather than the gantt.
These are real הפסקה events in the schedule, tagged so a pull-back
archives them alongside everything else the cut created.

#### coversPrayer

> **coversPrayer**: `null` \| `string`

Prayer this break was positioned to cover, when any.

#### kind

> **kind**: `string`

#### title

> **title**: `string`

***

### isRecurrenceEcho

> **isRecurrenceEcho**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:199](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L199)

True when this is a recurrence echo rather than the mapped start day.

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:195](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L195)

ISO date (yyyy-MM-dd) of the occurrence — also the recurrence disambiguator.

***

### parked?

> `optional` **parked?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:212](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L212)

Cut straight into the schedule's unassigned box (ארגז) instead of onto
the grid: a week-only mapping under `parkWeekOnly`, or work that did not
fit its day under the `park` overflow resolution. Its times are only a
placeholder.

***

### spilledFromDayId?

> `optional` **spilledFromDayId?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:205](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L205)

Set when the balancer relocated this occurrence off the day it was mapped
to — the id of that original day. Drives the preview's moved/unmoved
highlight.

***

### startTime

> **startTime**: `Date`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:196](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-planner.ts#L196)
