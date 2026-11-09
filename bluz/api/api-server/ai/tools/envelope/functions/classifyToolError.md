[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/envelope](../index.md) / classifyToolError

# Function: classifyToolError()

> **classifyToolError**(`error`): `object`

Defined in: [ui/src/api-server/ai/tools/envelope.ts:74](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/ai/tools/envelope.ts#L74)

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
