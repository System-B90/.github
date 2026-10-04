[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-models](../index.md) / ApiAiModelsResponse

# Type Alias: ApiAiModelsResponse

> **ApiAiModelsResponse** = `object`

Defined in: [ui/src/api-shared/types/ai-models.ts:16](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/ai-models.ts#L16)

## Properties

### defaultModel

> **defaultModel**: `string`

Defined in: [ui/src/api-shared/types/ai-models.ts:20](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/ai-models.ts#L20)

The server's configured `AI_MODEL`.

***

### error?

> `optional` **error?**: `string`

Defined in: [ui/src/api-shared/types/ai-models.ts:22](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/ai-models.ts#L22)

Why the list is empty, when listing failed.

***

### models

> **models**: [`AiModelInfo`](AiModelInfo.md)[]

Defined in: [ui/src/api-shared/types/ai-models.ts:18](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-shared/types/ai-models.ts#L18)

Empty when the backend cannot list models; the UI falls back to free text.
