[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / collectBreakWindows

# Function: collectBreakWindows()

> **collectBreakWindows**(`events`): [`BreakWindow`](../type-aliases/BreakWindow.md)[]

Defined in: [ui/src/api-shared/break-windows.ts:54](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/break-windows.ts#L54)

Extracts every break event in `events` as a scoped window. Pass the complete
event set, not a filtered/visible subset — a break hidden by a filter still
interrupts the day.

## Parameters

### events

`Iterable`\<[`SplittableEvent`](../type-aliases/SplittableEvent.md)\>

## Returns

[`BreakWindow`](../type-aliases/BreakWindow.md)[]
