[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/ai](../index.md) / fetchAiTools

# Function: fetchAiTools()

> **fetchAiTools**(): `Promise`\<\{ `enabled`: `boolean`; `model`: `string` \| `null`; `tools`: [`AiToolSummary`](../../../api-shared/types/ai/type-aliases/AiToolSummary.md)[]; \}\>

Defined in: [ui/src/api-client/ai.ts:100](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-client/ai.ts#L100)

Whether this deployment has AI wired up, plus what the assistant can do.

Only a genuine "not configured" answer resolves to `enabled: false` — a
transient fault (5xx, network drop) throws instead, so a caller can retry
rather than have the assistant look permanently unavailable for a blip.

## Returns

`Promise`\<\{ `enabled`: `boolean`; `model`: `string` \| `null`; `tools`: [`AiToolSummary`](../../../api-shared/types/ai/type-aliases/AiToolSummary.md)[]; \}\>
