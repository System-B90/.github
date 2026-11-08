[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/models](../index.md) / discoverModels

# Function: discoverModels()

> **discoverModels**(`provider`, `now?`): `Promise`\<[`ApiAiModelsResponse`](../../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>

Defined in: [ui/src/api-server/ai/models.ts:33](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/models.ts#L33)

The backend's models, cached for a few minutes.

## Parameters

### provider

[`AiProvider`](../../provider/type-aliases/AiProvider.md)

### now?

`number` = `...`

## Returns

`Promise`\<[`ApiAiModelsResponse`](../../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>

`models` empty plus `error` when the backend cannot list them.
