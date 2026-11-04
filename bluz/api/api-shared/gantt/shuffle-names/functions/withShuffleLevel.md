[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / withShuffleLevel

# Function: withShuffleLevel()

> **withShuffleLevel**(`levels`, `name`, `level`): [`ShuffleLevels`](../type-aliases/ShuffleLevels.md)

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:203](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/gantt/shuffle-names.ts#L203)

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
