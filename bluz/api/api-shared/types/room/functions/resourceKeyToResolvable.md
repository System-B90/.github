[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/room](../index.md) / resourceKeyToResolvable

# Function: resourceKeyToResolvable()

> **resourceKeyToResolvable**(`key`): [`ResolvableRoom`](../type-aliases/ResolvableRoom.md)

Defined in: [ui/src/api-shared/types/room.ts:95](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/room.ts#L95)

Inverse of [roomLikeToResourceKey](roomLikeToResourceKey.md). Splits on the first `:` only, so
ids containing further separators survive intact. Hive ids are numeric and
are coerced back to `number` to match [ResolvableRoom](../type-aliases/ResolvableRoom.md).

## Parameters

### key

`string`

## Returns

[`ResolvableRoom`](../type-aliases/ResolvableRoom.md)
