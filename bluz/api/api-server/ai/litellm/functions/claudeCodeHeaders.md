[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / claudeCodeHeaders

# Function: claudeCodeHeaders()

> **claudeCodeHeaders**(`customHeaders`): `Record`\<`string`, `string`\>

Defined in: [ui/src/api-server/ai/litellm.ts:53](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/litellm.ts#L53)

Claude Code's headers with `ANTHROPIC_CUSTOM_HEADERS` on top. Names are
compared case-insensitively, so a custom `user-agent` replaces the default.

## Parameters

### customHeaders

`string` \| `undefined`

## Returns

`Record`\<`string`, `string`\>
