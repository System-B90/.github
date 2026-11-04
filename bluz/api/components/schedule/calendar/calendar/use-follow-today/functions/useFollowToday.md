[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/use-follow-today](../index.md) / useFollowToday

# Function: useFollowToday()

> **useFollowToday**(`view`, `setCurrentDate`): `void`

Defined in: [ui/src/components/schedule/calendar/calendar/use-follow-today.ts:23](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/use-follow-today.ts#L23)

Keeps the staff calendar on the server's "today" across midnight.

Reads the server clock (see [useServerClockSync](../../../../../base/use-server-clock-sync/functions/useServerClockSync.md)); when the server's
day (Jerusalem time) changes, moves the view to the new day — if it was
showing the day that just ended. A view the user paged elsewhere stays put.
The first sync does the same for the device's idea of today, so a laptop
whose clock sits across midnight from the server opens on the server's day.

## Parameters

### view

`View`

### setCurrentDate

`Dispatch`\<`SetStateAction`\<`Date`\>\>

## Returns

`void`
