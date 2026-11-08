[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / escapeRegex

# Function: escapeRegex()

> **escapeRegex**(`value`): `string`

Defined in: [ui/src/api-server/ai/tools/common.ts:64](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/tools/common.ts#L64)

Escapes text before it reaches Mongo's `$regex`. The model relays whatever
the user typed, so an unescaped value both widens the search silently (`.`,
`|`) and exposes the server to catastrophic backtracking (`(a+)+b`).

## Parameters

### value

`string`

## Returns

`string`
