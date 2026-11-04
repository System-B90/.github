[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / parseCustomHeaders

# Function: parseCustomHeaders()

> **parseCustomHeaders**(`raw`): `Record`\<`string`, `string`\>

Defined in: [ui/src/api-server/ai/litellm.ts:36](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/ai/litellm.ts#L36)

`ANTHROPIC_CUSTOM_HEADERS` as Claude Code reads it: one `Name: Value` per
line. Lines without a name and a colon are skipped.

## Parameters

### raw

`string` \| `undefined`

## Returns

`Record`\<`string`, `string`\>
