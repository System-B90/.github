[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/cut-dialog/ReloadScheduleDialog](../index.md) / ReloadScheduleDialogProps

# Type Alias: ReloadScheduleDialogProps

> **ReloadScheduleDialogProps** = `object`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:43](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L43)

"עדכון הלו״ז לפי הגאנט" — reconciles an already-cut schedule with the
current gantt. Non-conflicting changes are applied immediately; events a
person edited after the cut are listed here so the user can decide, per
event, whether the gantt version should win after all.

## Properties

### curriculumId

> **curriculumId**: [`GanttCurriculumId`](../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:45](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L45)

***

### curriculumTitle?

> `optional` **curriculumTitle?**: `string`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:46](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L46)

***

### onClose

> **onClose**: () => `void`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:47](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L47)

#### Returns

`void`

***

### onSuccess?

> `optional` **onSuccess?**: () => `void`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:49](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L49)

Fired after any successful apply so the caller can refresh its view.

#### Returns

`void`

***

### open

> **open**: `boolean`

Defined in: [ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx:44](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/cut-dialog/ReloadScheduleDialog.tsx#L44)
