[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/bucket-fill](../index.md) / emptyRunAround

# Function: emptyRunAround()

> **emptyRunAround**(`at`, `obstacles`, `window`): [`Interval`](../../../../../../api-shared/interval-layout/type-aliases/Interval.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar/bucket-fill.ts:12](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/calendar/bucket-fill.ts#L12)

The empty run of time around `at`, like a paint-bucket fill: it spreads up
to the nearest obstacle ending before `at` (or the window's start) and down
to the nearest one starting after it (or the window's end).

## Parameters

### at

`number`

Epoch ms the fill starts from.

### obstacles

`Iterable`\<[`Interval`](../../../../../../api-shared/interval-layout/type-aliases/Interval.md)\>

What is drawn in the same column; any order.

### window

[`Interval`](../../../../../../api-shared/interval-layout/type-aliases/Interval.md)

The column's visible bounds.

## Returns

[`Interval`](../../../../../../api-shared/interval-layout/type-aliases/Interval.md) \| `null`

The gap, or null when `at` is covered or outside the window.
