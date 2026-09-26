[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/envelope](../index.md) / errorEnvelope

# Function: errorEnvelope()

> **errorEnvelope**(`toolName`, `error`, `tool?`): [`AiToolEnvelope`](../type-aliases/AiToolEnvelope.md)

Defined in: [ui/src/api-server/ai/tools/envelope.ts:157](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/envelope.ts#L157)

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
