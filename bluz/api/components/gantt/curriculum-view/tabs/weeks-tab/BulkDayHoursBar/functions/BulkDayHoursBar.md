[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/weeks-tab/BulkDayHoursBar](../index.md) / BulkDayHoursBar

# Function: BulkDayHoursBar()

> **BulkDayHoursBar**(): `Element` \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/weeks-tab/BulkDayHoursBar.tsx:31](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/curriculum-view/tabs/weeks-tab/BulkDayHoursBar.tsx#L31)

Sets the working hours of every shift-selected day at once (#476). This
replaced the per-column override inputs in the header row, which could only
ever write one weekday across *all* weeks — the common case (a stretch of
days around a holiday, one short week) had no expression at all.

Rendered only while something is selected, so it costs no space otherwise.

## Returns

`Element` \| `null`
