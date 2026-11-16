[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/envelope](../index.md) / errorEnvelope

# Function: errorEnvelope()

> **errorEnvelope**(`toolName`, `error`, `tool?`): [`AiToolEnvelope`](../type-aliases/AiToolEnvelope.md)

Defined in: [ui/src/api-server/ai/tools/envelope.ts:179](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/ai/tools/envelope.ts#L179)

Wraps a failed call, with the recovery path for its failure class.

## Parameters

### toolName

`string`

### error

`unknown`

### tool?

[`AiTool`](../../types/type-aliases/AiTool.md)\<`any`\>

## Returns

[`AiToolEnvelope`](../type-aliases/AiToolEnvelope.md)
