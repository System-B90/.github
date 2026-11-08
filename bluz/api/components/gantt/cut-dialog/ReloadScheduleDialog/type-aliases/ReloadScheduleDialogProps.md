[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/cut-dialog/ReloadScheduleDialog](../index.md) / ReloadScheduleDialogProps

# Type Alias: ReloadScheduleDialogProps

> **ReloadScheduleDialogProps** = `object`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:55](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L55)

"עדכון הלו״ז לפי הגאנט" — reconciles an already-cut schedule with the
current gantt. Non-conflicting changes are applied immediately; events a
person edited after the cut are listed here so the user can decide, per
event, whether the gantt version should win after all.

Always runs forced: an unmapped event or unsatisfied recurrence is skipped
rather than blocking the update. The extra "the gantt is incomplete" step
that used to ask first was dropped — a reload is cheap to run again once
the gantt is finished. A missing start date still fails, as a plain error.

## Properties

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:57](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L57)

***

### curriculumTitle?

> `optional` **curriculumTitle?**: `string`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:58](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L58)

***

### onClose

> **onClose**: () => `void`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:59](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L59)

#### Returns

`void`

***

### onSuccess?

> `optional` **onSuccess?**: () => `void`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:61](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L61)

Fired after any successful apply so the caller can refresh its view.

#### Returns

`void`

***

### open

> **open**: `boolean`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:56](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L56)
