[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/module-dialog](../index.md) / ModuleDialogProps

# Type Alias: ModuleDialogProps

> **ModuleDialogProps** = `object` & `DialogProps`

Defined in: [ui/src/components/gantt/module-dialog/index.tsx:55](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/gantt/module-dialog/index.tsx#L55)

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
