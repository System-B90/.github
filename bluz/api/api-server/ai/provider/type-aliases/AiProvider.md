[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiProvider

# Type Alias: AiProvider

> **AiProvider** = `object`

Defined in: [ui/src/api-server/ai/provider.ts:56](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/provider.ts#L56)

## Properties

### chat

> **chat**: (`request`) => `Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

Defined in: [ui/src/api-server/ai/provider.ts:63](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/provider.ts#L63)

One-shot completion, for callers with nothing to stream to.

#### Parameters

##### request

[`AiChatRequest`](AiChatRequest.md)

#### Returns

`Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

***

### defaultModel

> `readonly` **defaultModel**: `string`

Defined in: [ui/src/api-server/ai/provider.ts:60](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/provider.ts#L60)

Model used when a request does not name one.

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/provider.ts:58](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/provider.ts#L58)

Stable identifier, used in logs and in `AI_PROVIDER`.

***

### streamChat

> **streamChat**: (`request`) => `AsyncIterable`\<[`AiProviderEvent`](AiProviderEvent.md)\>

Defined in: [ui/src/api-server/ai/provider.ts:69](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/provider.ts#L69)

Incremental completion. Yields text as it arrives and terminates with a
single `final` frame carrying tool calls and usage.

#### Parameters

##### request

[`AiChatRequest`](AiChatRequest.md)

#### Returns

`AsyncIterable`\<[`AiProviderEvent`](AiProviderEvent.md)\>
