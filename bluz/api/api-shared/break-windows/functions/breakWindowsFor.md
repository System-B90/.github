[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / breakWindowsFor

# Function: breakWindowsFor()

> **breakWindowsFor**(`event`, `windows`): [`Interval`](../../interval-layout/type-aliases/Interval.md)[]

Defined in: [ui/src/api-shared/break-windows.ts:109](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/break-windows.ts#L109)

The windows that actually interrupt `event`: scoped to its audience, and
empty whenever the event doesn't split at all (flag off, or a break event
itself — breaks never split over each other).

## Parameters

### event

[`SplittableEvent`](../type-aliases/SplittableEvent.md)

### windows

readonly [`BreakWindow`](../type-aliases/BreakWindow.md)[]

## Returns

[`Interval`](../../interval-layout/type-aliases/Interval.md)[]
