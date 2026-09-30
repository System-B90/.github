[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/recurrence-exception](../index.md) / GanttEventRecurrenceException

# Type Alias: GanttEventRecurrenceException

> **GanttEventRecurrenceException** = `object`

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:11](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L11)

Marks a single occurrence day of a recurring event as excepted within a
curriculum: the event no longer echoes onto that day, either because the
occurrence was deleted outright or materialized into its own standalone
event.

## Properties

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../curriculum/type-aliases/GanttCurriculumId.md)

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:13](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L13)

***

### dayId

> **dayId**: [`GanttDayId`](../../day/type-aliases/GanttDayId.md)

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:15](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L15)

***

### eventId

> **eventId**: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md)

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:14](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L14)

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:12](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L12)

***

### materializedEventId?

> `optional` **materializedEventId?**: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md) \| `null`

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:20](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L20)

Event the occurrence was materialized into, or null when it was merely
skipped. Only skipped occurrences can be restored (#469).
