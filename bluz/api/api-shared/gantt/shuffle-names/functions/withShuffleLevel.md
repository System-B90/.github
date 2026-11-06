[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / withShuffleLevel

# Function: withShuffleLevel()

> **withShuffleLevel**(`levels`, `name`, `level`): [`ShuffleLevels`](../type-aliases/ShuffleLevels.md)

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:201](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/gantt/shuffle-names.ts#L201)

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
