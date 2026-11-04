[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/room](../index.md) / roomToResolvable

# Function: roomToResolvable()

> **roomToResolvable**\<`T`\>(`room`): `Extract`\<\{ `id`: `number`; `source`: [`Hive`](../enumerations/RoomSource.md#hive); \}, \{ `source`: `T`\[`"source"`\]; \}\> \| `Extract`\<\{ `id`: `string`; `source`: [`Custom`](../enumerations/RoomSource.md#custom); \}, \{ `source`: `T`\[`"source"`\]; \}\>

Defined in: [ui/src/api-shared/types/room.ts:64](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/room.ts#L64)

## Type Parameters

### T

`T` *extends* [`Room`](../type-aliases/Room.md)

## Parameters

### room

`T`

## Returns

`Extract`\<\{ `id`: `number`; `source`: [`Hive`](../enumerations/RoomSource.md#hive); \}, \{ `source`: `T`\[`"source"`\]; \}\> \| `Extract`\<\{ `id`: `string`; `source`: [`Custom`](../enumerations/RoomSource.md#custom); \}, \{ `source`: `T`\[`"source"`\]; \}\>
