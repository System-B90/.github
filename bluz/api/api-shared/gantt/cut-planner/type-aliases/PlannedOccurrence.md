[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / PlannedOccurrence

# Type Alias: PlannedOccurrence

> **PlannedOccurrence** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:171](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-shared/gantt/cut-planner.ts#L171)

## Properties

### endTime

> **endTime**: `Date`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:176](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-shared/gantt/cut-planner.ts#L176)

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:172](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-shared/gantt/cut-planner.ts#L172)

***

### generatedBreak?

> `optional` **generatedBreak?**: `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:190](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-shared/gantt/cut-planner.ts#L190)

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

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:178](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-shared/gantt/cut-planner.ts#L178)

True when this is a recurrence echo rather than the mapped start day.

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:174](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-shared/gantt/cut-planner.ts#L174)

ISO date (yyyy-MM-dd) of the occurrence — also the recurrence disambiguator.

***

### spilledFromDayId?

> `optional` **spilledFromDayId?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:184](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-shared/gantt/cut-planner.ts#L184)

Set when the balancer relocated this occurrence off the day it was mapped
to — the id of that original day. Drives the preview's moved/unmoved
highlight.

***

### startTime

> **startTime**: `Date`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:175](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-shared/gantt/cut-planner.ts#L175)
