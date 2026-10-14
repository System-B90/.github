[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/models](../index.md) / discoverModels

# Function: discoverModels()

> **discoverModels**(`provider`, `now?`): `Promise`\<[`ApiAiModelsResponse`](../../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>

Defined in: [ui/src/api-server/ai/models.ts:32](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-server/ai/models.ts#L32)

The backend's models, cached for a few minutes.

## Parameters

### provider

[`AiProvider`](../../provider/type-aliases/AiProvider.md)

### now?

`number` = `...`

## Returns

`Promise`\<[`ApiAiModelsResponse`](../../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>

`models` empty plus `error` when the backend cannot list them.
