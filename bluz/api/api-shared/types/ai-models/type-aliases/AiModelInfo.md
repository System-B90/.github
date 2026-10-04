[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-models](../index.md) / AiModelInfo

# Type Alias: AiModelInfo

> **AiModelInfo** = `object`

Defined in: [ui/src/api-shared/types/ai-models.ts:9](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-models.ts#L9)

Model discovery for OpenAI-compatible backends (#779).

`AI_MODEL` used to be a string an operator had to type exactly; a typo only
surfaced as a 404 at chat time. The backend's own model list now feeds the
personal-settings dropdown and the self-test's "is AI_MODEL real" check.

## Properties

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/ai-models.ts:11](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-models.ts#L11)

The slug sent as `model` in chat requests.

***

### name?

> `optional` **name?**: `string`

Defined in: [ui/src/api-shared/types/ai-models.ts:13](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/ai-models.ts#L13)

Display name, when the backend reports one (Open WebUI does).
