[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/ask-user](../index.md) / normalizeChoiceOptions

# Function: normalizeChoiceOptions()

> **normalizeChoiceOptions**(`options`): [`AiChoiceOption`](../../../../../api-shared/types/ai/type-aliases/AiChoiceOption.md)[]

Defined in: [ui/src/api-server/ai/tools/ask-user.ts:33](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/tools/ask-user.ts#L33)

Normalises what the model produced into something renderable. A missing
`value`, a duplicate, or an over-long list is a model mistake that must not
reach the UI as a broken button row.

## Parameters

### options

[`AiChoiceOption`](../../../../../api-shared/types/ai/type-aliases/AiChoiceOption.md)[] \| `undefined`

## Returns

[`AiChoiceOption`](../../../../../api-shared/types/ai/type-aliases/AiChoiceOption.md)[]
