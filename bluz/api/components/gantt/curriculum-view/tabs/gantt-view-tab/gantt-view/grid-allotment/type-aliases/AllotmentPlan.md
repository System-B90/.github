[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment](../index.md) / AllotmentPlan

# Type Alias: AllotmentPlan

> **AllotmentPlan** = \{ `dayId`: `string`; `kind`: `"create"`; `minutes`: `number`; \} \| \{ `dayId`: `string`; `kind`: `"materialize"`; `minutes`: `number`; \} \| \{ `kind`: `"none"`; \} \| \{ `dayId`: `string`; `fromDayId`: `string`; `kind`: `"outside"`; `minutes`: `number`; \} \| \{ `changes`: `object`[]; `kind`: `"set"`; \} \| \{ `dayIds`: `string`[]; `kind`: `"zero"`; \}

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts:28](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts#L28)

What a week-cell edit does to the event's mappings:
- `set`: change minutes on mappings already in the week.
- `zero`: the week was set to 0 — ask whether to keep 0-minute mappings or remove them.
- `create`: add a mapping on a day of the week.
- `outside`: the event sits in another week and may not split — ask whether
  to move its mapping here or turn on splitting across weeks.
- `materialize`: the week only holds a recurrence echo — turn that occurrence
  into its own event, then allot the minutes to it.
