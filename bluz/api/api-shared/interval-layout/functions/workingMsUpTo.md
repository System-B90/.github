[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/interval-layout](../index.md) / workingMsUpTo

# Function: workingMsUpTo()

> **workingMsUpTo**(`start`, `point`, `windows`, `options?`): `number`

Defined in: [ui/src/api-shared/interval-layout.ts:175](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/interval-layout.ts#L175)

Inverse of [layoutAroundWindows](layoutAroundWindows.md): how much *working* time a run
starting at `start` has consumed by the time the clock reaches `point`.
Window time is not work, so it doesn't count. Used to translate a resize
handle dropped anywhere on screen back into a net duration.

## Parameters

### start

`number`

Epoch ms the run begins at.

### point

`number`

Epoch ms to measure up to.

### windows

`Iterable`\<[`Interval`](../type-aliases/Interval.md)\>

Blocked windows (any order; overlaps are fine).

### options?

[`LayoutOptions`](../type-aliases/LayoutOptions.md) = `{}`

## Returns

`number`

Net working milliseconds in `[start, point]`; never negative.
