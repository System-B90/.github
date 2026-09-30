[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / PlannedOccurrence

# Type Alias: PlannedOccurrence

> **PlannedOccurrence** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:174](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L174)

## Properties

### endTime

> **endTime**: `Date`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:179](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L179)

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:175](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L175)

***

### generatedBreak?

> `optional` **generatedBreak?**: `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:193](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L193)

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

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:181](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L181)

True when this is a recurrence echo rather than the mapped start day.

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:177](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L177)

ISO date (yyyy-MM-dd) of the occurrence — also the recurrence disambiguator.

***

### spilledFromDayId?

> `optional` **spilledFromDayId?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:187](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L187)

Set when the balancer relocated this occurrence off the day it was mapped
to — the id of that original day. Drives the preview's moved/unmoved
highlight.

***

### startTime

> **startTime**: `Date`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:178](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L178)
