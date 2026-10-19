[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / retagShuffles

# Function: retagShuffles()

> **retagShuffles**(`tags`, `removed`, `renames`): `string`[]

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:98](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/shuffle-names.ts#L98)

A module/event's tags after a shuffle edit: removed names dropped, renamed
ones rewritten. Shared by the server cascade and the client's local mirror.

## Parameters

### tags

`string`[]

### removed

`string`[]

### renames

[`ShuffleRenames`](../type-aliases/ShuffleRenames.md)

## Returns

`string`[]
