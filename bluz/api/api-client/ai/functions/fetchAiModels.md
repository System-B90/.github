[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/ai](../index.md) / fetchAiModels

# Function: fetchAiModels()

> **fetchAiModels**(): `Promise`\<[`ApiAiModelsResponse`](../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>

Defined in: [ui/src/api-client/ai.ts:72](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-client/ai.ts#L72)

Models the configured AI backend offers (#779). Never throws: an empty list
(with `error`) just leaves the settings field free-text.

## Returns

`Promise`\<[`ApiAiModelsResponse`](../../../api-shared/types/ai-models/type-aliases/ApiAiModelsResponse.md)\>
