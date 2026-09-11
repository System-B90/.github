[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/interval-layout](../index.md) / normalizeWindows

# Function: normalizeWindows()

> **normalizeWindows**(`windows`): [`Interval`](../type-aliases/Interval.md)[]

Defined in: [ui/src/api-shared/interval-layout.ts:34](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/interval-layout.ts#L34)

Sorts windows and merges every overlapping or touching pair, so downstream
walks can assume a strictly increasing, non-overlapping sequence. Empty and
inverted windows are dropped.

## Parameters

### windows

`Iterable`\<[`Interval`](../type-aliases/Interval.md)\>

## Returns

[`Interval`](../type-aliases/Interval.md)[]
