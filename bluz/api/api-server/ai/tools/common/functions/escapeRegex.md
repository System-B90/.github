[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / escapeRegex

# Function: escapeRegex()

> **escapeRegex**(`value`): `string`

Defined in: [ui/src/api-server/ai/tools/common.ts:64](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/ai/tools/common.ts#L64)

Escapes text before it reaches Mongo's `$regex`. The model relays whatever
the user typed, so an unescaped value both widens the search silently (`.`,
`|`) and exposes the server to catastrophic backtracking (`(a+)+b`).

## Parameters

### value

`string`

## Returns

`string`
