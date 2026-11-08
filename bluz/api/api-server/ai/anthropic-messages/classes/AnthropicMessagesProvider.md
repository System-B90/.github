[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/anthropic-messages](../index.md) / AnthropicMessagesProvider

# Class: AnthropicMessagesProvider

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:212](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/anthropic-messages.ts#L212)

## Extended by

- [`LiteLlmProvider`](../../litellm/classes/LiteLlmProvider.md)

## Implements

- [`AiProvider`](../../provider/type-aliases/AiProvider.md)

## Constructors

### Constructor

> **new AnthropicMessagesProvider**(`options`): `AnthropicMessagesProvider`

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:221](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/anthropic-messages.ts#L221)

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

Sent on every request. Never the credential: `Authorization` and
`x-api-key` here are dropped, so the selected key (personal token,
static key or helper) is always the one sent.

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

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:215](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/anthropic-messages.ts#L215)

Model used when a request does not name one.

#### Implementation of

`AiProvider.defaultModel`

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:214](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/anthropic-messages.ts#L214)

Stable identifier, used in logs and in `AI_PROVIDER`.

#### Implementation of

`AiProvider.name`

## Methods

### chat()

> **chat**(`request`): `Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:248](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/anthropic-messages.ts#L248)

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

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:346](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/anthropic-messages.ts#L346)

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

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:276](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/anthropic-messages.ts#L276)

Incremental completion. Yields text as it arrives and terminates with a
single `final` frame carrying tool calls and usage.

#### Parameters

##### request

[`AiChatRequest`](../../provider/type-aliases/AiChatRequest.md)

#### Returns

`AsyncIterable`\<[`AiProviderEvent`](../../provider/type-aliases/AiProviderEvent.md)\>

#### Implementation of

`AiProvider.streamChat`
