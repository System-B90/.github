[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCutPreviewOccurrence

# Type Alias: ApiCutPreviewOccurrence

> **ApiCutPreviewOccurrence** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:145](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L145)

A single dated, timed occurrence in a cut preview — the pure planner's
output enriched with display metadata. Dates are ISO strings so the payload
survives JSON transport; the client re-hydrates with dayjs.

## Properties

### breakKind

> **breakKind**: `null` \| `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:169](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L169)

Which break rule produced it (`BreakKind`), or null for a real event.

***

### endTime

> **endTime**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:163](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L163)

ISO datetime.

***

### eventType

> **eventType**: [`ModuleEventType`](../../models/event/enumerations/ModuleEventType.md)

Defined in: [ui/src/api-shared/types/gantt/cut.ts:149](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L149)

ModuleEventType of the source gantt event.

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:146](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L146)

***

### hiveSubjectId

> **hiveSubjectId**: `null` \| `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:155](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L155)

Hive subject id the source gantt event is linked to, or null when the
event is a non-Hive placeholder. Lets the preview color occurrences by
their real subject color, matching the actual schedule (#331).

***

### isGeneratedBreak

> **isGeneratedBreak**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:167](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L167)

True for a break the post-pass invented rather than a gantt event.

***

### isRecurrenceEcho

> **isRecurrenceEcho**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:165](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L165)

True when this is a recurrence echo rather than the mapped start day.

***

### moduleTitle

> **moduleTitle**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:157](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L157)

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:159](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L159)

ISO date (yyyy-MM-dd) of the occurrence.

***

### parked

> **parked**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:176](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L176)

Lands in the schedule's unassigned box (ארגז), not on the grid.

***

### spilled

> **spilled**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:174](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L174)

True when the balancer relocated this occurrence off the day it was
mapped to. Drives the preview's moved/unmoved highlight.

***

### startTime

> **startTime**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:161](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L161)

ISO datetime.

***

### syllabusTitle

> **syllabusTitle**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:156](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L156)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:147](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/cut.ts#L147)
