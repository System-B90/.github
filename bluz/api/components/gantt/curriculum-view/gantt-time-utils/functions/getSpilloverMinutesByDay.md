[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / getSpilloverMinutesByDay

# Function: getSpilloverMinutesByDay()

> **getSpilloverMinutesByDay**(`spans`): `Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), `number`\>

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:314](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L314)

Per-day scheduled minutes with multi-day spillover applied: each event
contributes only the minutes it consumes on that specific day, so hours
spilled onto subsequent days are subtracted from the start day and added
to the days they land on.

## Parameters

### spans

`Record`\<`string`, [`EventDaySpan`](../type-aliases/EventDaySpan.md)\>

## Returns

`Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), `number`\>
