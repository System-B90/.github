[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCutPreviewOccurrence

# Type Alias: ApiCutPreviewOccurrence

> **ApiCutPreviewOccurrence** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:118](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L118)

A single dated, timed occurrence in a cut preview — the pure planner's
output enriched with display metadata. Dates are ISO strings so the payload
survives JSON transport; the client re-hydrates with dayjs.

## Properties

### breakKind

> **breakKind**: `null` \| `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:142](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L142)

Which break rule produced it (`BreakKind`), or null for a real event.

***

### endTime

> **endTime**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:136](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L136)

ISO datetime.

***

### eventType

> **eventType**: [`ModuleEventType`](../../models/event/enumerations/ModuleEventType.md)

Defined in: [ui/src/api-shared/types/gantt/cut.ts:122](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L122)

ModuleEventType of the source gantt event.

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:119](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L119)

***

### hiveSubjectId

> **hiveSubjectId**: `null` \| `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:128](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L128)

Hive subject id the source gantt event is linked to, or null when the
event is a non-Hive placeholder. Lets the preview color occurrences by
their real subject color, matching the actual schedule (#331).

***

### isGeneratedBreak

> **isGeneratedBreak**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:140](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L140)

True for a break the post-pass invented rather than a gantt event.

***

### isRecurrenceEcho

> **isRecurrenceEcho**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:138](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L138)

True when this is a recurrence echo rather than the mapped start day.

***

### moduleTitle

> **moduleTitle**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:130](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L130)

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:132](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L132)

ISO date (yyyy-MM-dd) of the occurrence.

***

### spilled

> **spilled**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:147](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L147)

True when the balancer relocated this occurrence off the day it was
mapped to. Drives the preview's moved/unmoved highlight.

***

### startTime

> **startTime**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:134](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L134)

ISO datetime.

***

### syllabusTitle

> **syllabusTitle**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:129](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L129)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:120](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L120)
