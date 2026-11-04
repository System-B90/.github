[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / parseCustomHeaders

# Function: parseCustomHeaders()

> **parseCustomHeaders**(`raw`): `Record`\<`string`, `string`\>

Defined in: [ui/src/api-server/ai/litellm.ts:36](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/litellm.ts#L36)

`ANTHROPIC_CUSTOM_HEADERS` as Claude Code reads it: one `Name: Value` per
line. Lines without a name and a colon are skipped.

## Parameters

### raw

`string` \| `undefined`

## Returns

`Record`\<`string`, `string`\>
