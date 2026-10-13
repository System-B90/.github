[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / PlannedOccurrence

# Type Alias: PlannedOccurrence

> **PlannedOccurrence** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:176](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L176)

## Properties

### endTime

> **endTime**: `Date`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:181](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L181)

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:177](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L177)

***

### generatedBreak?

> `optional` **generatedBreak?**: `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:195](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L195)

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

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:183](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L183)

True when this is a recurrence echo rather than the mapped start day.

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:179](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L179)

ISO date (yyyy-MM-dd) of the occurrence — also the recurrence disambiguator.

***

### spilledFromDayId?

> `optional` **spilledFromDayId?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:189](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L189)

Set when the balancer relocated this occurrence off the day it was mapped
to — the id of that original day. Drives the preview's moved/unmoved
highlight.

***

### startTime

> **startTime**: `Date`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:180](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L180)
