[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/curriculum-day-module-mapping](../index.md) / GanttCurriculumEventDayMapping

# Type Alias: GanttCurriculumEventDayMapping

> **GanttCurriculumEventDayMapping** = `object`

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:15](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L15)

The date mapping of a module.
This interface represents an instance of a module or a specific event of a module in a curriculum, set to be at a specific day in a specific week.
Each mapping is unique to a event?<->module<->curriculum<->day(<->week)
An order field is available in order to maintain a sorted array of mappings which are all temporarily allocated on the same day.
This is used when zooming in and out of views.

## Properties

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../curriculum/type-aliases/GanttCurriculumId.md)

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:19](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L19)

***

### dayId

> **dayId**: [`GanttDayId`](../../day/type-aliases/GanttDayId.md)

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:18](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L18)

***

### eventId?

> `optional` **eventId?**: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md) \| `null`

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:17](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L17)

***

### moduleId

> **moduleId**: [`GanttModuleId`](../../shared/type-aliases/GanttModuleId.md)

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:16](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L16)

***

### sortOrder

> **sortOrder**: `number`

Defined in: [ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts:20](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/curriculum-day-module-mapping.ts#L20)
