[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / pickDefined

# Function: pickDefined()

> **pickDefined**\<`T`, `K`\>(`args`, `keys`): `Partial`\<`Pick`\<`T`, `K`\>\>

Defined in: [ui/src/api-server/ai/tools/common.ts:141](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/tools/common.ts#L141)

Copies only the keys present in `args` — a partial patch, never a reset.

## Type Parameters

### T

`T` *extends* `Record`\<`string`, `unknown`\>

### K

`K` *extends* `string` \| `number` \| `symbol`

## Parameters

### args

`T`

### keys

readonly `K`[]

## Returns

`Partial`\<`Pick`\<`T`, `K`\>\>
