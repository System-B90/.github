[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/module-dialog](../index.md) / ModuleDialogProps

# Type Alias: ModuleDialogProps

> **ModuleDialogProps** = `object` & `DialogProps`

Defined in: [ui/src/components/gantt/module-dialog/index.tsx:56](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/module-dialog/index.tsx#L56)

## Type Declaration

### covered?

> `optional` **covered?**: `boolean`

Another gantt dialog (the event dialog) is open on top. Its delete is
hidden so only the top layer's delete is ever on screen (#834).

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
