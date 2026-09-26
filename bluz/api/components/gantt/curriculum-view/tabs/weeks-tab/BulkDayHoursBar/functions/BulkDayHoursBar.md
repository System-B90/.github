[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/weeks-tab/BulkDayHoursBar](../index.md) / BulkDayHoursBar

# Function: BulkDayHoursBar()

> **BulkDayHoursBar**(): `Element` \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/weeks-tab/BulkDayHoursBar.tsx:30](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/tabs/weeks-tab/BulkDayHoursBar.tsx#L30)

Sets the working hours of every shift-selected day at once (#476). This
replaced the per-column override inputs in the header row, which could only
ever write one weekday across *all* weeks — the common case (a stretch of
days around a holiday, one short week) had no expression at all.

Rendered only while something is selected, so it costs no space otherwise.

## Returns

`Element` \| `null`
