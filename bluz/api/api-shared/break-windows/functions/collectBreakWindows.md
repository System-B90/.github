[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / collectBreakWindows

# Function: collectBreakWindows()

> **collectBreakWindows**(`events`): [`BreakWindow`](../type-aliases/BreakWindow.md)[]

Defined in: [ui/src/api-shared/break-windows.ts:59](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/break-windows.ts#L59)

Extracts every break event in `events` as a scoped window. Pass the complete
event set, not a filtered/visible subset — a break hidden by a filter still
interrupts the day.

## Parameters

### events

`Iterable`\<[`SplittableEvent`](../type-aliases/SplittableEvent.md)\>

## Returns

[`BreakWindow`](../type-aliases/BreakWindow.md)[]
