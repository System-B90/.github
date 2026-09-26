[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCutPreviewOccurrence

# Type Alias: ApiCutPreviewOccurrence

> **ApiCutPreviewOccurrence** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:93](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L93)

A single dated, timed occurrence in a cut preview — the pure planner's
output enriched with display metadata. Dates are ISO strings so the payload
survives JSON transport; the client re-hydrates with dayjs.

## Properties

### breakKind

> **breakKind**: `null` \| `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:117](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L117)

Which break rule produced it (`BreakKind`), or null for a real event.

***

### endTime

> **endTime**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:111](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L111)

ISO datetime.

***

### eventType

> **eventType**: [`ModuleEventType`](../../models/event/enumerations/ModuleEventType.md)

Defined in: [ui/src/api-shared/types/gantt/cut.ts:97](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L97)

ModuleEventType of the source gantt event.

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:94](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L94)

***

### hiveSubjectId

> **hiveSubjectId**: `null` \| `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:103](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L103)

Hive subject id the source gantt event is linked to, or null when the
event is a non-Hive placeholder. Lets the preview color occurrences by
their real subject color, matching the actual schedule (#331).

***

### isGeneratedBreak

> **isGeneratedBreak**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:115](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L115)

True for a break the post-pass invented rather than a gantt event.

***

### isRecurrenceEcho

> **isRecurrenceEcho**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:113](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L113)

True when this is a recurrence echo rather than the mapped start day.

***

### moduleTitle

> **moduleTitle**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:105](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L105)

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:107](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L107)

ISO date (yyyy-MM-dd) of the occurrence.

***

### spilled

> **spilled**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:122](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L122)

True when the balancer relocated this occurrence off the day it was
mapped to. Drives the preview's moved/unmoved highlight.

***

### startTime

> **startTime**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:109](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L109)

ISO datetime.

***

### syllabusTitle

> **syllabusTitle**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:104](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L104)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:95](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L95)
