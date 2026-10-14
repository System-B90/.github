[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/syllabus-dialog](../index.md) / SyllabusDialogProps

# Type Alias: SyllabusDialogProps

> **SyllabusDialogProps** = `object`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:44](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/syllabus-dialog/index.tsx#L44)

## Properties

### covered?

> `optional` **covered?**: `boolean`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:54](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/syllabus-dialog/index.tsx#L54)

A module/event dialog is open on top. The dialog then hides entirely
(#884) and stays mounted, so it comes back as it was when the top layer
closes. Before #884 it only hid its destructive action (#834).

***

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:47](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/syllabus-dialog/index.tsx#L47)

***

### draft?

> `optional` **draft?**: `boolean`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:60](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/syllabus-dialog/index.tsx#L60)

Open on a syllabus that doesn't exist yet (#881). Nothing is saved until
the name is committed; then the syllabus is created and the dialog
carries on editing it through `onDraftCreated`.

***

### onDraftCreated?

> `optional` **onDraftCreated?**: (`syllabusId`) => `void`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:61](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/syllabus-dialog/index.tsx#L61)

#### Parameters

##### syllabusId

[`GanttSyllabusId`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md)

#### Returns

`void`

***

### open

> **open**: `boolean`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:45](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/syllabus-dialog/index.tsx#L45)

***

### setOpen

> **setOpen**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:46](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/syllabus-dialog/index.tsx#L46)

***

### syllabusId

> **syllabusId**: [`GanttSyllabusId`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md) \| `null`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:48](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/syllabus-dialog/index.tsx#L48)
