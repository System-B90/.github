[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / withShuffleLevel

# Function: withShuffleLevel()

> **withShuffleLevel**(`levels`, `name`, `level`): [`ShuffleLevels`](../type-aliases/ShuffleLevels.md)

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:203](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-shared/gantt/shuffle-names.ts#L203)

`levels` with `name` set to `level`, or without `name` for "" — the level is
optional, and no level is stored as no entry (the map holds valid levels only).

## Parameters

### levels

[`ShuffleLevels`](../type-aliases/ShuffleLevels.md)

### name

`string`

### level

`""` \| `"מתחילים"` \| `"בינוניים"` \| `"מתקדמים"`

## Returns

[`ShuffleLevels`](../type-aliases/ShuffleLevels.md)
