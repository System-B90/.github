[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / splitEventAcrossBreaks

# Function: splitEventAcrossBreaks()

> **splitEventAcrossBreaks**(`event`, `windows`, `options?`): [`Interval`](../../interval-layout/type-aliases/Interval.md)[]

Defined in: [ui/src/api-shared/break-windows.ts:189](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/break-windows.ts#L189)

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
