[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / splitEventAcrossBreaks

# Function: splitEventAcrossBreaks()

> **splitEventAcrossBreaks**(`event`, `windows`, `options?`): [`Interval`](../../interval-layout/type-aliases/Interval.md)[]

Defined in: [ui/src/api-shared/break-windows.ts:153](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/break-windows.ts#L153)

Lays an event out across the breaks that interrupt it.

## Parameters

### event

[`SplittableEvent`](../type-aliases/SplittableEvent.md)

The event to lay out.

### windows

readonly [`BreakWindow`](../type-aliases/BreakWindow.md)[]

All break windows in play (see [collectBreakWindows](collectBreakWindows.md)).

### options?

[`LayoutOptions`](../../interval-layout/type-aliases/LayoutOptions.md)

## Returns

[`Interval`](../../interval-layout/type-aliases/Interval.md)[]

One or more segments covering the event's working time; always
         exactly one segment for a non-splitting event.
