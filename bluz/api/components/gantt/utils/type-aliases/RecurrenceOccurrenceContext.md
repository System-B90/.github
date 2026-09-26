[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / RecurrenceOccurrenceContext

# Type Alias: RecurrenceOccurrenceContext

> **RecurrenceOccurrenceContext** = `object`

Defined in: [ui/src/components/gantt/utils.tsx:38](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/utils.tsx#L38)

Placement/exception data needed to count how many times a recurring event
actually occurs on the timeline. Omitted ⇒ every event counts once,
matching the pre-recurrence-aware behavior (e.g. before placement exists).

## Properties

### exceptions

> **exceptions**: `Record`\<`string`, [`GanttEventRecurrenceException`](../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)\>

Defined in: [ui/src/components/gantt/utils.tsx:41](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/utils.tsx#L41)

***

### linearDays

> **linearDays**: `string`[]

Defined in: [ui/src/components/gantt/utils.tsx:43](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/utils.tsx#L43)

Timeline day ids in chronological order.

***

### mappings

> **mappings**: `Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

Defined in: [ui/src/components/gantt/utils.tsx:40](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/utils.tsx#L40)
