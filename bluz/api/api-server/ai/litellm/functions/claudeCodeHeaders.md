[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / claudeCodeHeaders

# Function: claudeCodeHeaders()

> **claudeCodeHeaders**(`customHeaders`): `Record`\<`string`, `string`\>

Defined in: [ui/src/api-server/ai/litellm.ts:53](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/litellm.ts#L53)

Claude Code's headers with `ANTHROPIC_CUSTOM_HEADERS` on top. Names are
compared case-insensitively, so a custom `user-agent` replaces the default.

## Parameters

### customHeaders

`string` \| `undefined`

## Returns

`Record`\<`string`, `string`\>
