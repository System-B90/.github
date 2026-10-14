[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / breakWindowsReaching

# Function: breakWindowsReaching()

> **breakWindowsReaching**(`event`, `windows`, `options?`): [`Interval`](../../interval-layout/type-aliases/Interval.md)[]

Defined in: [ui/src/api-shared/break-windows.ts:122](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/break-windows.ts#L122)

[breakWindowsFor](breakWindowsFor.md), narrowed to the windows the event can actually run
into from where it starts now (#927). The cheap time test runs before the
room/course match, so a week's worth of breaks costs a few comparisons per
event instead of an audience check each.

The reach is an upper bound: every window the event jumps can push its end
out by that window's length, plus a skipped sliver (shorter than
`minSegmentMs`) before it. Windows are walked in start order, so the first
one past the reach ends the walk.

## Parameters

### event

[`SplittableEvent`](../type-aliases/SplittableEvent.md)

### windows

readonly [`BreakWindow`](../type-aliases/BreakWindow.md)[]

### options?

[`LayoutOptions`](../../interval-layout/type-aliases/LayoutOptions.md) = `{}`

## Returns

[`Interval`](../../interval-layout/type-aliases/Interval.md)[]
