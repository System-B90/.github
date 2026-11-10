[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / withShuffleLevel

# Function: withShuffleLevel()

> **withShuffleLevel**(`levels`, `name`, `level`): [`ShuffleLevels`](../type-aliases/ShuffleLevels.md)

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:201](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/gantt/shuffle-names.ts#L201)

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
