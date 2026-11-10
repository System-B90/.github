[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/mappings/types](../index.md) / GanttMappingAction

# Type Alias: GanttMappingAction

> **GanttMappingAction** = \{ `payload`: `Pick`\<[`GanttCurriculumEventDayMapping`](../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md), `"dayId"` \| `"eventId"` \| `"moduleId"`\>; `type`: `"DELETE_MAPPING"`; \} \| \{ `payload`: `boolean`; `type`: `"SET_LOADING"`; \} \| \{ `payload`: [`GanttCurriculumEventDayMapping`](../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)[]; `type`: `"SET_MAPPINGS"`; \} \| \{ `payload`: [`GanttCurriculumEventDayMapping`](../../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md); `type`: `"UPSERT_MAPPING"`; \}

Defined in: [ui/src/components/gantt/state/mappings/types.ts:14](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/state/mappings/types.ts#L14)
