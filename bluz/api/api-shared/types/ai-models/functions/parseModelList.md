[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-models](../index.md) / parseModelList

# Function: parseModelList()

> **parseModelList**(`body`): [`AiModelInfo`](../type-aliases/AiModelInfo.md)[]

Defined in: [ui/src/api-shared/types/ai-models.ts:32](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/ai-models.ts#L32)

Normalises a `/models` response. OpenAI and most gateways answer
`{ data: [{ id }] }`; Open WebUI's `/api/models` answers the same envelope
with a `name` beside each `id`, and some servers return a bare array.

## Parameters

### body

`unknown`

The parsed JSON body.

## Returns

[`AiModelInfo`](../type-aliases/AiModelInfo.md)[]

De-duplicated models, sorted by id; unknown shapes yield none.
