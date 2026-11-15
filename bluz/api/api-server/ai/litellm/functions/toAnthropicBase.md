[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / toAnthropicBase

# Function: toAnthropicBase()

> **toAnthropicBase**(`url`): `string`

Defined in: [ui/src/api-server/ai/litellm.ts:70](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/ai/litellm.ts#L70)

`ANTHROPIC_BASE_URL` as Claude Code reads it: the LiteLLM root or its
`/anthropic` pass-through, with `/v1/messages` appended. A pasted `/v1`
suffix is dropped so it is not doubled.

## Parameters

### url

`string`

## Returns

`string`
