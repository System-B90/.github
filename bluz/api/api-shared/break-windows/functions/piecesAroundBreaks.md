[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / piecesAroundBreaks

# Function: piecesAroundBreaks()

> **piecesAroundBreaks**(`event`, `windows`): [`Interval`](../../interval-layout/type-aliases/Interval.md)[]

Defined in: [ui/src/api-shared/break-windows.ts:129](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/break-windows.ts#L129)

The blocks an event becomes when split into separate events around the
breaks that reach it (#1017) — the same blocks the schedule draws. A
split-enabled event keeps its working time and jumps each break, as it is
laid out; any other event loses the stretch a break covers. Applies to an
event whether or not its split flag is on; breaks are never split.

## Parameters

### event

[`SplittableEvent`](../type-aliases/SplittableEvent.md)

The event to split.

### windows

readonly [`BreakWindow`](../type-aliases/BreakWindow.md)[]

Every break window of the day (see [collectBreakWindows](collectBreakWindows.md)).

## Returns

[`Interval`](../../interval-layout/type-aliases/Interval.md)[]

The blocks, ordered; a single block when no break interrupts it.
