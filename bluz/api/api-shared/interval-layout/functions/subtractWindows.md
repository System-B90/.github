[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/interval-layout](../index.md) / subtractWindows

# Function: subtractWindows()

> **subtractWindows**(`start`, `end`, `windows`, `options?`): [`Interval`](../type-aliases/Interval.md)[]

Defined in: [ui/src/api-shared/interval-layout.ts:129](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/interval-layout.ts#L129)

What is left of `[start, end]` once every window is cut out of it. Unlike
[layoutAroundWindows](layoutAroundWindows.md) the span does not grow: window time is lost,
not pushed later. Leftovers shorter than `minSegmentMs` are dropped.

## Parameters

### start

`number`

Epoch ms the span begins at.

### end

`number`

Epoch ms the span ends at.

### windows

`Iterable`\<[`Interval`](../type-aliases/Interval.md)\>

Windows to cut out (any order; overlaps are fine).

### options?

[`LayoutOptions`](../type-aliases/LayoutOptions.md) = `{}`

## Returns

[`Interval`](../type-aliases/Interval.md)[]

The remaining pieces, ordered; empty when windows cover it all.
