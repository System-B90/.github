[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/cut-dialog/ReloadScheduleDialog](../index.md) / ReloadScheduleDialogProps

# Type Alias: ReloadScheduleDialogProps

> **ReloadScheduleDialogProps** = `object`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:48](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L48)

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

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:50](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L50)

***

### curriculumTitle?

> `optional` **curriculumTitle?**: `string`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:51](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L51)

***

### onClose

> **onClose**: () => `void`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:52](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L52)

#### Returns

`void`

***

### onSuccess?

> `optional` **onSuccess?**: () => `void`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:54](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L54)

Fired after any successful apply so the caller can refresh its view.

#### Returns

`void`

***

### open

> **open**: `boolean`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:49](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L49)
