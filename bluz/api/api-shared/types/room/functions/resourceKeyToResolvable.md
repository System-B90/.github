[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/room](../index.md) / resourceKeyToResolvable

# Function: resourceKeyToResolvable()

> **resourceKeyToResolvable**(`key`): [`ResolvableRoom`](../type-aliases/ResolvableRoom.md)

Defined in: [ui/src/api-shared/types/room.ts:100](https://github.com/System-B90/Bluz/blob/ef5f1592ad9f013b150ea581b494f4fff71a8490/ui/src/api-shared/types/room.ts#L100)

Inverse of [roomLikeToResourceKey](roomLikeToResourceKey.md). Splits on the first `:` only, so
ids containing further separators survive intact. Hive ids are numeric and
are coerced back to `number` to match [ResolvableRoom](../type-aliases/ResolvableRoom.md).

## Parameters

### key

`string`

## Returns

[`ResolvableRoom`](../type-aliases/ResolvableRoom.md)
