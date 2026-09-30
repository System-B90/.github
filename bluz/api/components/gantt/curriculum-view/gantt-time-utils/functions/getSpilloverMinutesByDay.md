[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / getSpilloverMinutesByDay

# Function: getSpilloverMinutesByDay()

> **getSpilloverMinutesByDay**(`spans`): `Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), `number`\>

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:377](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L377)

Per-day scheduled minutes with multi-day spillover applied: each event
contributes only the minutes it consumes on that specific day, so hours
spilled onto subsequent days are subtracted from the start day and added
to the days they land on.

## Parameters

### spans

`Record`\<`string`, [`EventDaySpan`](../type-aliases/EventDaySpan.md)\>

## Returns

`Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), `number`\>
