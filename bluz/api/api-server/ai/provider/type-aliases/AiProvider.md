[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiProvider

# Type Alias: AiProvider

> **AiProvider** = `object`

Defined in: [ui/src/api-server/ai/provider.ts:57](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/provider.ts#L57)

## Properties

### chat

> **chat**: (`request`) => `Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

Defined in: [ui/src/api-server/ai/provider.ts:64](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/provider.ts#L64)

One-shot completion, for callers with nothing to stream to.

#### Parameters

##### request

[`AiChatRequest`](AiChatRequest.md)

#### Returns

`Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

***

### defaultModel

> `readonly` **defaultModel**: `string`

Defined in: [ui/src/api-server/ai/provider.ts:61](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/provider.ts#L61)

Model used when a request does not name one.

***

### listModels?

> `optional` **listModels?**: (`signal?`) => `Promise`\<[`AiModelInfo`](../../../../api-shared/types/ai-models/type-aliases/AiModelInfo.md)[]\>

Defined in: [ui/src/api-server/ai/provider.ts:76](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/provider.ts#L76)

Models the backend offers (#779). Optional: a backend that cannot list
them simply leaves the settings field free-text.

#### Parameters

##### signal?

`AbortSignal`

#### Returns

`Promise`\<[`AiModelInfo`](../../../../api-shared/types/ai-models/type-aliases/AiModelInfo.md)[]\>

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/provider.ts:59](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/provider.ts#L59)

Stable identifier, used in logs and in `AI_PROVIDER`.

***

### streamChat

> **streamChat**: (`request`) => `AsyncIterable`\<[`AiProviderEvent`](AiProviderEvent.md)\>

Defined in: [ui/src/api-server/ai/provider.ts:70](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/provider.ts#L70)

Incremental completion. Yields text as it arrives and terminates with a
single `final` frame carrying tool calls and usage.

#### Parameters

##### request

[`AiChatRequest`](AiChatRequest.md)

#### Returns

`AsyncIterable`\<[`AiProviderEvent`](AiProviderEvent.md)\>
