[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/recurrence](../index.md) / getOccurrenceDayIdForWeek

# Function: getOccurrenceDayIdForWeek()

> **getOccurrenceDayIdForWeek**(`weekDayIds`, `startDow`, `dayIndexOf`): `string` \| `null`

Defined in: [ui/src/api-shared/gantt/recurrence.ts:121](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/recurrence.ts#L121)

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
