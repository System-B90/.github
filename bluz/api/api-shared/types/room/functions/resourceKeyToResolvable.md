[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/room](../index.md) / resourceKeyToResolvable

# Function: resourceKeyToResolvable()

> **resourceKeyToResolvable**(`key`): [`ResolvableRoom`](../type-aliases/ResolvableRoom.md)

Defined in: [ui/src/api-shared/types/room.ts:92](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/room.ts#L92)

Inverse of [roomLikeToResourceKey](roomLikeToResourceKey.md). Splits on the first `:` only, so
ids containing further separators survive intact. Hive ids are numeric and
are coerced back to `number` to match [ResolvableRoom](../type-aliases/ResolvableRoom.md).

## Parameters

### key

`string`

## Returns

[`ResolvableRoom`](../type-aliases/ResolvableRoom.md)
