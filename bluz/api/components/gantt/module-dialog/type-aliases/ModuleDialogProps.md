[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/module-dialog](../index.md) / ModuleDialogProps

# Type Alias: ModuleDialogProps

> **ModuleDialogProps** = `object` & `DialogProps`

Defined in: [ui/src/components/gantt/module-dialog/index.tsx:56](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/module-dialog/index.tsx#L56)

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
