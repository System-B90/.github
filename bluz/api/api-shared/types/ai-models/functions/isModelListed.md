[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-models](../index.md) / isModelListed

# Function: isModelListed()

> **isModelListed**(`model`, `models`): `boolean`

Defined in: [ui/src/api-shared/types/ai-models.ts:58](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/types/ai-models.ts#L58)

Whether a configured model slug is among the listed ones. An empty list
means "unknown", not "absent", so it never triggers a warning.

## Parameters

### model

`string`

### models

[`AiModelInfo`](../type-aliases/AiModelInfo.md)[]

## Returns

`boolean`
