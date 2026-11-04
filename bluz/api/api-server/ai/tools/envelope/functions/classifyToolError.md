[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/envelope](../index.md) / classifyToolError

# Function: classifyToolError()

> **classifyToolError**(`error`): `object`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:74](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/tools/envelope.ts#L74)

Classifies a thrown error into something the model can act on.

`ClientApiError` is the app's "the caller was wrong" class, which for a tool
call means the *model* was wrong — the one case where retrying with fixed
arguments is the right move. Anything else is a dependency fault.

## Parameters

### error

`unknown`

## Returns

`object`

### kind

> **kind**: [`AiToolErrorKind`](../../types/enumerations/AiToolErrorKind.md)

### message

> **message**: `string`
