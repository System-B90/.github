[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-models](../index.md) / isModelListed

# Function: isModelListed()

> **isModelListed**(`model`, `models`): `boolean`

Defined in: [ui/src/api-shared/types/ai-models.ts:60](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/ai-models.ts#L60)

Whether a configured model slug is among the listed ones. An empty list
means "unknown", not "absent", so it never triggers a warning.

## Parameters

### model

`string`

### models

[`AiModelInfo`](../type-aliases/AiModelInfo.md)[]

## Returns

`boolean`
