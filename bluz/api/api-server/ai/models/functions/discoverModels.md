[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/models](../index.md) / discoverModels

# Function: discoverModels()

> **discoverModels**(`provider`, `now?`): `Promise`\<[`ApiAiModelsResponse`](../../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>

Defined in: [ui/src/api-server/ai/models.ts:32](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/models.ts#L32)

The backend's models, cached for a few minutes.

## Parameters

### provider

[`AiProvider`](../../provider/type-aliases/AiProvider.md)

### now?

`number` = `...`

## Returns

`Promise`\<[`ApiAiModelsResponse`](../../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>

`models` empty plus `error` when the backend cannot list them.
