[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / claudeCodeHeaders

# Function: claudeCodeHeaders()

> **claudeCodeHeaders**(`customHeaders`): `Record`\<`string`, `string`\>

Defined in: [ui/src/api-server/ai/litellm.ts:53](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/ai/litellm.ts#L53)

Claude Code's headers with `ANTHROPIC_CUSTOM_HEADERS` on top. Names are
compared case-insensitively, so a custom `user-agent` replaces the default.

## Parameters

### customHeaders

`string` \| `undefined`

## Returns

`Record`\<`string`, `string`\>
