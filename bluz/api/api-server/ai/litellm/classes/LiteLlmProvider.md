[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / LiteLlmProvider

# Class: LiteLlmProvider

Defined in: [ui/src/api-server/ai/litellm.ts:82](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/litellm.ts#L82)

## Extends

- [`AnthropicMessagesProvider`](../../anthropic-messages/classes/AnthropicMessagesProvider.md)

## Constructors

### Constructor

> **new LiteLlmProvider**(`apiKeyOverride?`): `LiteLlmProvider`

Defined in: [ui/src/api-server/ai/litellm.ts:87](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/litellm.ts#L87)

#### Parameters

##### apiKeyOverride?

`string`

A user's own LiteLLM key; skips the helper.

#### Returns

`LiteLlmProvider`

#### Overrides

[`AnthropicMessagesProvider`](../../anthropic-messages/classes/AnthropicMessagesProvider.md).[`constructor`](../../anthropic-messages/classes/AnthropicMessagesProvider.md#constructor)

## Properties

### defaultModel

> `readonly` **defaultModel**: `string`

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:187](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/anthropic-messages.ts#L187)

Model used when a request does not name one.

#### Inherited from

[`AnthropicMessagesProvider`](../../anthropic-messages/classes/AnthropicMessagesProvider.md).[`defaultModel`](../../anthropic-messages/classes/AnthropicMessagesProvider.md#defaultmodel)

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:186](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/anthropic-messages.ts#L186)

Stable identifier, used in logs and in `AI_PROVIDER`.

#### Inherited from

[`AnthropicMessagesProvider`](../../anthropic-messages/classes/AnthropicMessagesProvider.md).[`name`](../../anthropic-messages/classes/AnthropicMessagesProvider.md#name)

## Methods

### chat()

> **chat**(`request`): `Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:216](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/anthropic-messages.ts#L216)

One-shot completion, for callers with nothing to stream to.

#### Parameters

##### request

[`AiChatRequest`](../../provider/type-aliases/AiChatRequest.md)

#### Returns

`Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

#### Inherited from

[`AnthropicMessagesProvider`](../../anthropic-messages/classes/AnthropicMessagesProvider.md).[`chat`](../../anthropic-messages/classes/AnthropicMessagesProvider.md#chat)

***

### listModels()

> **listModels**(`signal?`): `Promise`\<[`AiModelInfo`](../../../../api-shared/types/ai-models/type-aliases/AiModelInfo.md)[]\>

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:314](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/anthropic-messages.ts#L314)

Models the backend offers (#779). Optional: a backend that cannot list
them simply leaves the settings field free-text.

#### Parameters

##### signal?

`AbortSignal`

#### Returns

`Promise`\<[`AiModelInfo`](../../../../api-shared/types/ai-models/type-aliases/AiModelInfo.md)[]\>

#### Inherited from

[`AnthropicMessagesProvider`](../../anthropic-messages/classes/AnthropicMessagesProvider.md).[`listModels`](../../anthropic-messages/classes/AnthropicMessagesProvider.md#listmodels)

***

### streamChat()

> **streamChat**(`request`): `AsyncIterable`\<[`AiProviderEvent`](../../provider/type-aliases/AiProviderEvent.md)\>

Defined in: [ui/src/api-server/ai/anthropic-messages.ts:244](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/anthropic-messages.ts#L244)

Incremental completion. Yields text as it arrives and terminates with a
single `final` frame carrying tool calls and usage.

#### Parameters

##### request

[`AiChatRequest`](../../provider/type-aliases/AiChatRequest.md)

#### Returns

`AsyncIterable`\<[`AiProviderEvent`](../../provider/type-aliases/AiProviderEvent.md)\>

#### Inherited from

[`AnthropicMessagesProvider`](../../anthropic-messages/classes/AnthropicMessagesProvider.md).[`streamChat`](../../anthropic-messages/classes/AnthropicMessagesProvider.md#streamchat)
