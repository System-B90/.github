[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/curriculum-day-module-mapping](../index.md) / GanttCurriculumEventDayMapping

# Type Alias: GanttCurriculumEventDayMapping

> **GanttCurriculumEventDayMapping** = `object`

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:12](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L12)

The date mapping of a module.
This interface represents an instance of a module or a specific event of a module in a curriculum, set to be at a specific day in a specific week.
Each mapping is unique to a event?<->module<->curriculum<->day(<->week)
An order field is available in order to maintain a sorted array of mappings which are all temporarily allocated on the same day.
This is used when zooming in and out of views.

## Properties

### allottedMinutes?

> `optional` **allottedMinutes?**: `number`

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:22](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L22)

Minutes this event takes on this day: the single source of its
scheduled time. 0 keeps it documented but out of the cut.

***

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../curriculum/type-aliases/GanttCurriculumId.md)

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:16](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L16)

***

### dayId

> **dayId**: [`GanttDayId`](../../day/type-aliases/GanttDayId.md)

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:15](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L15)

***

### eventId?

> `optional` **eventId?**: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md) \| `null`

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:14](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L14)

***

### moduleId

> **moduleId**: [`GanttModuleId`](../../shared/type-aliases/GanttModuleId.md)

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:13](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L13)

***

### sortOrder

> **sortOrder**: `number`

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:17](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L17)

***

### weekOnly?

> `optional` **weekOnly?**: `boolean`

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:27](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L27)

Placed for the week, not a specific day (#964): `dayId` only holds it
inside the week. A week made only of these is cut onto Fri 16:00 – Sat.
