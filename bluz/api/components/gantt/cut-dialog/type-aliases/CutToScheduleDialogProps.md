[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/cut-dialog](../index.md) / CutToScheduleDialogProps

# Type Alias: CutToScheduleDialogProps

> **CutToScheduleDialogProps** = `object`

Defined in: [ui/src/components/gantt/cut-dialog/index.tsx:46](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/cut-dialog/index.tsx#L46)

## Properties

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

Defined in: [ui/src/components/gantt/cut-dialog/index.tsx:48](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/cut-dialog/index.tsx#L48)

***

### curriculumTitle?

> `optional` **curriculumTitle?**: `string`

Defined in: [ui/src/components/gantt/cut-dialog/index.tsx:49](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/cut-dialog/index.tsx#L49)

***

### onClose

> **onClose**: () => `void`

Defined in: [ui/src/components/gantt/cut-dialog/index.tsx:50](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/cut-dialog/index.tsx#L50)

#### Returns

`void`

***

### onSuccess?

> `optional` **onSuccess?**: () => `void`

Defined in: [ui/src/components/gantt/cut-dialog/index.tsx:52](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/cut-dialog/index.tsx#L52)

Fired after a successful cut so the caller can flip its cut state.

#### Returns

`void`

***

### open

> **open**: `boolean`

Defined in: [ui/src/components/gantt/cut-dialog/index.tsx:47](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/cut-dialog/index.tsx#L47)

***

### weekRequired?

> `optional` **weekRequired?**: `boolean`

Defined in: [ui/src/components/gantt/cut-dialog/index.tsx:57](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/cut-dialog/index.tsx#L57)

Only a single week may be cut (#970) — the curriculum is already cut, so
a whole-curriculum cut would be refused anyway.
