[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/syllabus-dialog](../index.md) / SyllabusDialogProps

# Type Alias: SyllabusDialogProps

> **SyllabusDialogProps** = `object`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:37](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/syllabus-dialog/index.tsx#L37)

## Properties

### covered?

> `optional` **covered?**: `boolean`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:47](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/syllabus-dialog/index.tsx#L47)

A module/event dialog is open on top. The dialog then hides entirely
(#884) and stays mounted, so it comes back as it was when the top layer
closes. Before #884 it only hid its destructive action (#834).

***

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:40](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/syllabus-dialog/index.tsx#L40)

***

### draft?

> `optional` **draft?**: `boolean`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:53](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/syllabus-dialog/index.tsx#L53)

Open on a syllabus that doesn't exist yet (#881). Nothing is saved until
the name is committed; then the syllabus is created and the dialog
carries on editing it through `onDraftCreated`.

***

### onDraftCreated?

> `optional` **onDraftCreated?**: (`syllabusId`) => `void`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:54](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/syllabus-dialog/index.tsx#L54)

#### Parameters

##### syllabusId

[`GanttSyllabusId`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md)

#### Returns

`void`

***

### open

> **open**: `boolean`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:38](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/syllabus-dialog/index.tsx#L38)

***

### setOpen

> **setOpen**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:39](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/syllabus-dialog/index.tsx#L39)

***

### syllabusId

> **syllabusId**: [`GanttSyllabusId`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md) \| `null`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:41](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/gantt/syllabus-dialog/index.tsx#L41)
