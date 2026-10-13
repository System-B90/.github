[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-models](../index.md) / isModelListed

# Function: isModelListed()

> **isModelListed**(`model`, `models`): `boolean`

Defined in: [ui/src/api-shared/types/ai-models.ts:56](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/ai-models.ts#L56)

Whether a configured model slug is among the listed ones. An empty list
means "unknown", not "absent", so it never triggers a warning.

## Parameters

### model

`string`

### models

[`AiModelInfo`](../type-aliases/AiModelInfo.md)[]

## Returns

`boolean`
