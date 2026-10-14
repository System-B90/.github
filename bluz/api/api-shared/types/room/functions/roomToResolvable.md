[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/room](../index.md) / roomToResolvable

# Function: roomToResolvable()

> **roomToResolvable**\<`T`\>(`room`): `Extract`\<\{ `id`: `number`; `source`: [`Hive`](../enumerations/RoomSource.md#hive); \}, \{ `source`: `T`\[`"source"`\]; \}\> \| `Extract`\<\{ `id`: `string`; `source`: [`Custom`](../enumerations/RoomSource.md#custom); \}, \{ `source`: `T`\[`"source"`\]; \}\>

Defined in: [ui/src/api-shared/types/room.ts:61](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/room.ts#L61)

## Type Parameters

### T

`T` *extends* [`Room`](../type-aliases/Room.md)

## Parameters

### room

`T`

## Returns

`Extract`\<\{ `id`: `number`; `source`: [`Hive`](../enumerations/RoomSource.md#hive); \}, \{ `source`: `T`\[`"source"`\]; \}\> \| `Extract`\<\{ `id`: `string`; `source`: [`Custom`](../enumerations/RoomSource.md#custom); \}, \{ `source`: `T`\[`"source"`\]; \}\>
