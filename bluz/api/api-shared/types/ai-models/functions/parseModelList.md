[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai-models](../index.md) / parseModelList

# Function: parseModelList()

> **parseModelList**(`body`): [`AiModelInfo`](../type-aliases/AiModelInfo.md)[]

Defined in: [ui/src/api-shared/types/ai-models.ts:34](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/ai-models.ts#L34)

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
