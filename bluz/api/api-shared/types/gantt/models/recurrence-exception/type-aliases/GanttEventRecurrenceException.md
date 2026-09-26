[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/recurrence-exception](../index.md) / GanttEventRecurrenceException

# Type Alias: GanttEventRecurrenceException

> **GanttEventRecurrenceException** = `object`

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:13](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L13)

Marks a single occurrence day of a recurring event as excepted within a
curriculum: the event no longer echoes onto that day, either because the
occurrence was deleted outright or materialized into its own standalone
event.

## Properties

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../curriculum/type-aliases/GanttCurriculumId.md)

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:15](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L15)

***

### dayId

> **dayId**: [`GanttDayId`](../../day/type-aliases/GanttDayId.md)

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:17](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L17)

***

### eventId

> **eventId**: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md)

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:16](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L16)

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:14](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L14)

***

### materializedEventId?

> `optional` **materializedEventId?**: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md) \| `null`

Defined in: [ui/src/api-shared/types/gantt/models/recurrence-exception.ts:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/recurrence-exception.ts#L22)

Event the occurrence was materialized into, or null when it was merely
skipped. Only skipped occurrences can be restored (#469).
