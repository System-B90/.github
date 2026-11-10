[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/ai](../index.md) / fetchAiModels

# Function: fetchAiModels()

> **fetchAiModels**(): `Promise`\<[`ApiAiModelsResponse`](../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>

Defined in: [ui/src/api-client/ai.ts:78](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-client/ai.ts#L78)

Models the configured AI backend offers (#779). Never throws: an empty list
(with `error`) just leaves the settings field free-text.

## Returns

`Promise`\<[`ApiAiModelsResponse`](../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>
