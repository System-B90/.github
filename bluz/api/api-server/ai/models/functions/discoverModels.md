[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/models](../index.md) / discoverModels

# Function: discoverModels()

> **discoverModels**(`provider`, `now?`): `Promise`\<[`ApiAiModelsResponse`](../../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>

Defined in: [ui/src/api-server/ai/models.ts:33](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/ai/models.ts#L33)

The backend's models, cached for a few minutes.

## Parameters

### provider

[`AiProvider`](../../provider/type-aliases/AiProvider.md)

### now?

`number` = `...`

## Returns

`Promise`\<[`ApiAiModelsResponse`](../../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>

`models` empty plus `error` when the backend cannot list them.
