[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/room](../index.md) / roomToResolvable

# Function: roomToResolvable()

> **roomToResolvable**\<`T`\>(`room`): `Extract`\<\{ `id`: `number`; `source`: [`Hive`](../enumerations/RoomSource.md#hive); \}, \{ `source`: `T`\[`"source"`\]; \}\> \| `Extract`\<\{ `id`: `string`; `source`: [`Custom`](../enumerations/RoomSource.md#custom); \}, \{ `source`: `T`\[`"source"`\]; \}\>

Defined in: [ui/src/api-shared/types/room.ts:64](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/room.ts#L64)

## Type Parameters

### T

`T` *extends* [`Room`](../type-aliases/Room.md)

## Parameters

### room

`T`

## Returns

`Extract`\<\{ `id`: `number`; `source`: [`Hive`](../enumerations/RoomSource.md#hive); \}, \{ `source`: `T`\[`"source"`\]; \}\> \| `Extract`\<\{ `id`: `string`; `source`: [`Custom`](../enumerations/RoomSource.md#custom); \}, \{ `source`: `T`\[`"source"`\]; \}\>
