[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiProvider

# Type Alias: AiProvider

> **AiProvider** = `object`

Defined in: [ui/src/api-server/ai/provider.ts:41](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L41)

## Properties

### chat

> **chat**: (`request`) => `Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

Defined in: [ui/src/api-server/ai/provider.ts:48](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L48)

One-shot completion, for callers with nothing to stream to.

#### Parameters

##### request

[`AiChatRequest`](AiChatRequest.md)

#### Returns

`Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

***

### defaultModel

> `readonly` **defaultModel**: `string`

Defined in: [ui/src/api-server/ai/provider.ts:45](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L45)

Model used when a request does not name one.

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/provider.ts:43](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L43)

Stable identifier, used in logs and in `AI_PROVIDER`.

***

### streamChat

> **streamChat**: (`request`) => `AsyncIterable`\<[`AiProviderEvent`](AiProviderEvent.md)\>

Defined in: [ui/src/api-server/ai/provider.ts:54](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L54)

Incremental completion. Yields text as it arrives and terminates with a
single `final` frame carrying tool calls and usage.

#### Parameters

##### request

[`AiChatRequest`](AiChatRequest.md)

#### Returns

`AsyncIterable`\<[`AiProviderEvent`](AiProviderEvent.md)\>
