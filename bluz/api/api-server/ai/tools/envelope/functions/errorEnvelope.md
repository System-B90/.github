[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/envelope](../index.md) / errorEnvelope

# Function: errorEnvelope()

> **errorEnvelope**(`toolName`, `error`, `tool?`): [`AiToolEnvelope`](../type-aliases/AiToolEnvelope.md)

Defined in: [ui/src/api-server/ai/tools/envelope.ts:165](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-server/ai/tools/envelope.ts#L165)

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
