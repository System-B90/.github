[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/parked-box/out-of-view](../index.md) / isOutsideDayView

# Function: isOutsideDayView()

> **isOutsideDayView**(`event`, `dayStart`, `dayEnd`): `boolean`

Defined in: [ui/src/components/schedule/calendar/parked-box/out-of-view.ts:44](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/parked-box/out-of-view.ts#L44)

Whether the event misses the schedule's day view on every day it spans: it
begins and ends outside the window the grid draws (the time settings' day
start–end), so no part of it is visible. Such an event can only be reached
from the side, and "לאסוף לארגז" gathers them into the box.

An end at or before the start ("00:00") is read as the end of the day, as
the grid itself does.

## Parameters

### event

`Pick`\<[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md), `"endTime"` \| `"startTime"`\>

### dayStart

`string`

The grid's first visible time, `HH:mm`.

### dayEnd

`string`

The grid's last visible time, `HH:mm`.

## Returns

`boolean`
