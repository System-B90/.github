[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / PlannedOccurrence

# Type Alias: PlannedOccurrence

> **PlannedOccurrence** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:169](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L169)

## Properties

### endTime

> **endTime**: `Date`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:174](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L174)

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:170](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L170)

***

### generatedBreak?

> `optional` **generatedBreak?**: `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:188](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L188)

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

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:176](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L176)

True when this is a recurrence echo rather than the mapped start day.

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:172](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L172)

ISO date (yyyy-MM-dd) of the occurrence — also the recurrence disambiguator.

***

### spilledFromDayId?

> `optional` **spilledFromDayId?**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:182](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L182)

Set when the balancer relocated this occurrence off the day it was mapped
to — the id of that original day. Drives the preview's moved/unmoved
highlight.

***

### startTime

> **startTime**: `Date`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:173](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L173)
