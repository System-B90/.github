[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/module-dialog](../index.md) / ModuleDialogProps

# Type Alias: ModuleDialogProps

> **ModuleDialogProps** = `object` & `DialogProps`

Defined in: [ui/src/components/gantt/module-dialog/index.tsx:54](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/module-dialog/index.tsx#L54)

## Type Declaration

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md) \| `null`

### focusEventId?

> `optional` **focusEventId?**: [`GanttEventId`](../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md) \| `null`

When set, the matching event row is scrolled into view and highlighted.

### moduleId

> **moduleId**: [`GanttModuleId`](../../../../api-shared/types/gantt/models/shared/type-aliases/GanttModuleId.md) \| `null`

### setOpen

> **setOpen**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

### syllabusId

> **syllabusId**: [`GanttSyllabusId`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md) \| `null`
