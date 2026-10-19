[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/parked-box/out-of-view](../index.md) / dayViewOn

# Function: dayViewOn()

> **dayViewOn**(`at`, `dayStart`, `dayEnd`): [`Interval`](../../../../../../api-shared/interval-layout/type-aliases/Interval.md)

Defined in: [ui/src/components/schedule/calendar/parked-box/out-of-view.ts:20](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/parked-box/out-of-view.ts#L20)

The window the grid draws on the day of `at` (Israel time): the time
settings' day start–end, with an end at or before the start ("00:00") read
as the end of the day.

## Parameters

### at

`number`

Epoch ms anywhere on the day.

### dayStart

`string`

The grid's first visible time, `HH:mm`.

### dayEnd

`string`

The grid's last visible time, `HH:mm`.

## Returns

[`Interval`](../../../../../../api-shared/interval-layout/type-aliases/Interval.md)
