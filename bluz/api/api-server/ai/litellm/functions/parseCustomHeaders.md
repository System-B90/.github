[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / parseCustomHeaders

# Function: parseCustomHeaders()

> **parseCustomHeaders**(`raw`): `Record`\<`string`, `string`\>

Defined in: [ui/src/api-server/ai/litellm.ts:36](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/litellm.ts#L36)

`ANTHROPIC_CUSTOM_HEADERS` as Claude Code reads it: one `Name: Value` per
line. Lines without a name and a colon are skipped.

## Parameters

### raw

`string` \| `undefined`

## Returns

`Record`\<`string`, `string`\>
