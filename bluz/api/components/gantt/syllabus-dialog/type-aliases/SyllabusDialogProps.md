[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/syllabus-dialog](../index.md) / SyllabusDialogProps

# Type Alias: SyllabusDialogProps

> **SyllabusDialogProps** = `object`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:45](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/syllabus-dialog/index.tsx#L45)

## Properties

### covered?

> `optional` **covered?**: `boolean`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:55](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/syllabus-dialog/index.tsx#L55)

A module/event dialog is open on top. The dialog then hides entirely
(#884) and stays mounted, so it comes back as it was when the top layer
closes. Before #884 it only hid its destructive action (#834).

***

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:48](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/syllabus-dialog/index.tsx#L48)

***

### draft?

> `optional` **draft?**: `boolean`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:61](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/syllabus-dialog/index.tsx#L61)

Open on a syllabus that doesn't exist yet (#881). Nothing is saved until
the name is committed; then the syllabus is created and the dialog
carries on editing it through `onDraftCreated`.

***

### onDraftCreated?

> `optional` **onDraftCreated?**: (`syllabusId`) => `void`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:62](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/syllabus-dialog/index.tsx#L62)

#### Parameters

##### syllabusId

[`GanttSyllabusId`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md)

#### Returns

`void`

***

### open

> **open**: `boolean`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:46](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/syllabus-dialog/index.tsx#L46)

***

### setOpen

> **setOpen**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:47](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/syllabus-dialog/index.tsx#L47)

***

### syllabusId

> **syllabusId**: [`GanttSyllabusId`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabusId.md) \| `null`

Defined in: [ui/src/components/gantt/syllabus-dialog/index.tsx:49](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/syllabus-dialog/index.tsx#L49)
