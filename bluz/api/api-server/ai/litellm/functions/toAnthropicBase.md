[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / toAnthropicBase

# Function: toAnthropicBase()

> **toAnthropicBase**(`url`): `string`

Defined in: [ui/src/api-server/ai/litellm.ts:70](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/litellm.ts#L70)

`ANTHROPIC_BASE_URL` as Claude Code reads it: the LiteLLM root or its
`/anthropic` pass-through, with `/v1/messages` appended. A pasted `/v1`
suffix is dropped so it is not doubled.

## Parameters

### url

`string`

## Returns

`string`
