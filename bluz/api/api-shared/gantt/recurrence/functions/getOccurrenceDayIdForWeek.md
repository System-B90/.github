[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/recurrence](../index.md) / getOccurrenceDayIdForWeek

# Function: getOccurrenceDayIdForWeek()

> **getOccurrenceDayIdForWeek**(`weekDayIds`, `startDow`, `dayIndexOf`): `string` \| `null`

Defined in: [ui/src/api-shared/gantt/recurrence.ts:121](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/gantt/recurrence.ts#L121)

The actual occurrence day within a given week's days for a weekly-recurring
event — the day matching the start day's weekday. The weekly timeline view
anchors an occurrence's visual block to the week's first day, but delete/
materialize actions need the real day id the occurrence falls on.

## Parameters

### weekDayIds

`string`[]

### startDow

[`GanttDayIndex`](../../../types/gantt/models/day/enumerations/GanttDayIndex.md) \| `undefined`

### dayIndexOf

(`dayId`) => [`GanttDayIndex`](../../../types/gantt/models/day/enumerations/GanttDayIndex.md) \| `undefined`

## Returns

`string` \| `null`
