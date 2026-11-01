[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / retagShuffles

# Function: retagShuffles()

> **retagShuffles**(`tags`, `removed`, `renames`): `string`[]

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:107](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/gantt/shuffle-names.ts#L107)

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
