[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/ai](../index.md) / fetchAiTools

# Function: fetchAiTools()

> **fetchAiTools**(): `Promise`\<\{ `enabled`: `boolean`; `model`: `string` \| `null`; `tools`: [`AiToolSummary`](../../../api-shared/types/ai/type-aliases/AiToolSummary.md)[]; \}\>

Defined in: [ui/src/api-client/ai.ts:90](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-client/ai.ts#L90)

Whether this deployment has AI wired up, plus what the assistant can do.

Only a genuine "not configured" answer resolves to `enabled: false` — a
transient fault (5xx, network drop) throws instead, so a caller can retry
rather than have the assistant look permanently unavailable for a blip.

## Returns

`Promise`\<\{ `enabled`: `boolean`; `model`: `string` \| `null`; `tools`: [`AiToolSummary`](../../../api-shared/types/ai/type-aliases/AiToolSummary.md)[]; \}\>
