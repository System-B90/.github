[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/weeks-tab/BulkDayHoursBar](../index.md) / BulkDayHoursBar

# Function: BulkDayHoursBar()

> **BulkDayHoursBar**(): `Element` \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/weeks-tab/BulkDayHoursBar.tsx:31](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/weeks-tab/BulkDayHoursBar.tsx#L31)

Sets the working hours of every shift-selected day at once (#476). This
replaced the per-column override inputs in the header row, which could only
ever write one weekday across *all* weeks — the common case (a stretch of
days around a holiday, one short week) had no expression at all.

Rendered only while something is selected, so it costs no space otherwise.

## Returns

`Element` \| `null`
