[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/builder-tab/components/dnd-types](../index.md) / DndDragEventActiveData

# Type Alias: DndDragEventActiveData

> **DndDragEventActiveData** = \{ `dayId?`: [`GanttDayId`](../../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md); `moduleId`: [`GanttModuleId`](../../../../../../../../api-shared/types/gantt/models/module/type-aliases/GanttModuleId.md); `syllabusId?`: `undefined`; `type`: `"MODULE"`; \} \| \{ `dayId?`: `undefined`; `moduleId`: [`GanttModuleId`](../../../../../../../../api-shared/types/gantt/models/module/type-aliases/GanttModuleId.md); `syllabusId`: [`GanttSyllabusId`](../../../../../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md); `type`: `"SORT_MODULE"`; \} \| \{ `dayId?`: [`GanttDayId`](../../../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md); `moduleId?`: `undefined`; `syllabusId`: [`GanttSyllabusId`](../../../../../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md); `type`: `"SYLLABUS"`; \}

Defined in: [ui/src/components/gantt/curriculum-view/tabs/builder-tab/components/dnd-types.ts:8](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/tabs/builder-tab/components/dnd-types.ts#L8)
