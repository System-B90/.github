[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / escapeRegex

# Function: escapeRegex()

> **escapeRegex**(`value`): `string`

Defined in: [ui/src/api-server/ai/tools/common.ts:62](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-server/ai/tools/common.ts#L62)

Escapes text before it reaches Mongo's `$regex`. The model relays whatever
the user typed, so an unescaped value both widens the search silently (`.`,
`|`) and exposes the server to catastrophic backtracking (`(a+)+b`).

## Parameters

### value

`string`

## Returns

`string`
