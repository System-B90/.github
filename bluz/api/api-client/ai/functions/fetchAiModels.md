[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/ai](../index.md) / fetchAiModels

# Function: fetchAiModels()

> **fetchAiModels**(): `Promise`\<[`ApiAiModelsResponse`](../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>

Defined in: [ui/src/api-client/ai.ts:78](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-client/ai.ts#L78)

Models the configured AI backend offers (#779). Never throws: an empty list
(with `error`) just leaves the settings field free-text.

## Returns

`Promise`\<[`ApiAiModelsResponse`](../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>
