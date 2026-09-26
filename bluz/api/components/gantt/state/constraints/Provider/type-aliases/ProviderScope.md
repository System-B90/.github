[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/Provider](../index.md) / ProviderScope

# Type Alias: ProviderScope

> **ProviderScope** = \{ `curriculumId`: [`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md); `type`: `"curriculum"`; \} \| \{ `curriculumId`: [`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md); `eventId`: [`GanttEventId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md); `moduleId`: [`GanttModuleId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttModuleId.md); `syllabusId`: `string`; `type`: `"event"`; \} \| \{ `curriculumId`: [`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md); `moduleId`: [`GanttModuleId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttModuleId.md); `syllabusId`: `string`; `type`: `"module"`; \}

Defined in: [ui/src/components/gantt/state/constraints/Provider.tsx:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/constraints/Provider.tsx#L25)

Defines the scope of the Gantt constraints provider context,
which can be scoped either curriculum-wide or to a specific module.
