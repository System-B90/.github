[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/anthropic-messages](../index.md) / AnthropicMessagesProvider

# Class: AnthropicMessagesProvider

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:184](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/anthropic-messages.ts#L184)

## Extended by

- [`LiteLlmProvider`](../../litellm/classes/LiteLlmProvider.md)

## Implements

- [`AiProvider`](../../provider/type-aliases/AiProvider.md)

## Constructors

### Constructor

> **new AnthropicMessagesProvider**(`options`): `AnthropicMessagesProvider`

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:193](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/anthropic-messages.ts#L193)

#### Parameters

##### options

###### apiKey

`string` \| [`AiKeySource`](../../key-source/type-aliases/AiKeySource.md)

###### baseUrl

`string`

Everything before `/v1/messages`, as in `ANTHROPIC_BASE_URL`.

###### defaultModel

`string`

###### headers?

`Record`\<`string`, `string`\>

Sent on every request after the auth headers (and may override them).

###### missingKeyMessage

`string`

Error shown when `apiKey` is empty — names the env var operators set.

###### name

`string`

#### Returns

`AnthropicMessagesProvider`

## Properties

### defaultModel

> `readonly` **defaultModel**: `string`

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:187](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/anthropic-messages.ts#L187)

Model used when a request does not name one.

#### Implementation of

`AiProvider.defaultModel`

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:186](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/anthropic-messages.ts#L186)

Stable identifier, used in logs and in `AI_PROVIDER`.

#### Implementation of

`AiProvider.name`

## Methods

### chat()

> **chat**(`request`): `Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:216](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/anthropic-messages.ts#L216)

One-shot completion, for callers with nothing to stream to.

#### Parameters

##### request

[`AiChatRequest`](../../provider/type-aliases/AiChatRequest.md)

#### Returns

`Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

#### Implementation of

`AiProvider.chat`

***

### listModels()

> **listModels**(`signal?`): `Promise`\<[`AiModelInfo`](../../../../api-shared/types/ai-models/type-aliases/AiModelInfo.md)[]\>

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:314](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/anthropic-messages.ts#L314)

Models the backend offers (#779). Optional: a backend that cannot list
them simply leaves the settings field free-text.

#### Parameters

##### signal?

`AbortSignal`

#### Returns

`Promise`\<[`AiModelInfo`](../../../../api-shared/types/ai-models/type-aliases/AiModelInfo.md)[]\>

#### Implementation of

`AiProvider.listModels`

***

### streamChat()

> **streamChat**(`request`): `AsyncIterable`\<[`AiProviderEvent`](../../provider/type-aliases/AiProviderEvent.md)\>

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:244](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/anthropic-messages.ts#L244)

Incremental completion. Yields text as it arrives and terminates with a
single `final` frame carrying tool calls and usage.

#### Parameters

##### request

[`AiChatRequest`](../../provider/type-aliases/AiChatRequest.md)

#### Returns

`AsyncIterable`\<[`AiProviderEvent`](../../provider/type-aliases/AiProviderEvent.md)\>

#### Implementation of

`AiProvider.streamChat`
