[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCutPreviewOccurrence

# Type Alias: ApiCutPreviewOccurrence

> **ApiCutPreviewOccurrence** = `object`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:123](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L123)

A single dated, timed occurrence in a cut preview — the pure planner's
output enriched with display metadata. Dates are ISO strings so the payload
survives JSON transport; the client re-hydrates with dayjs.

## Properties

### breakKind

> **breakKind**: `null` \| `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:147](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L147)

Which break rule produced it (`BreakKind`), or null for a real event.

***

### endTime

> **endTime**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:141](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L141)

ISO datetime.

***

### eventType

> **eventType**: [`ModuleEventType`](../../models/event/enumerations/ModuleEventType.md)

Defined in: [ui/src/api-shared/types/gantt/cut.ts:127](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L127)

ModuleEventType of the source gantt event.

***

### ganttEventId

> **ganttEventId**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:124](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L124)

***

### hiveSubjectId

> **hiveSubjectId**: `null` \| `number`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:133](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L133)

Hive subject id the source gantt event is linked to, or null when the
event is a non-Hive placeholder. Lets the preview color occurrences by
their real subject color, matching the actual schedule (#331).

***

### isGeneratedBreak

> **isGeneratedBreak**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:145](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L145)

True for a break the post-pass invented rather than a gantt event.

***

### isRecurrenceEcho

> **isRecurrenceEcho**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:143](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L143)

True when this is a recurrence echo rather than the mapped start day.

***

### moduleTitle

> **moduleTitle**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:135](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L135)

***

### occurrenceDate

> **occurrenceDate**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:137](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L137)

ISO date (yyyy-MM-dd) of the occurrence.

***

### spilled

> **spilled**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:152](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L152)

True when the balancer relocated this occurrence off the day it was
mapped to. Drives the preview's moved/unmoved highlight.

***

### startTime

> **startTime**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:139](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L139)

ISO datetime.

***

### syllabusTitle

> **syllabusTitle**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:134](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L134)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/types/gantt/cut.ts:125](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/cut.ts#L125)
