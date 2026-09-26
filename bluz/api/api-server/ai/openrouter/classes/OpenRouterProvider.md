[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/openrouter](../index.md) / OpenRouterProvider

# Class: OpenRouterProvider

Defined in: [ui/src/api-server/ai/openrouter.ts:16](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/openrouter.ts#L16)

## Extends

- [`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md)

## Constructors

### Constructor

> **new OpenRouterProvider**(`options`): `OpenRouterProvider`

Defined in: [ui/src/api-server/ai/openrouter.ts:17](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/openrouter.ts#L17)

#### Parameters

##### options

###### apiKey

`string`

###### baseUrl?

`string`

###### defaultModel?

`string`

###### referer?

`string`

Attribution headers; OpenRouter uses them for rate-limit tiers.

###### title?

`string`

#### Returns

`OpenRouterProvider`

#### Overrides

[`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md).[`constructor`](../../openai-compatible/classes/OpenAiCompatibleProvider.md#constructor)

## Properties

### defaultModel

> `readonly` **defaultModel**: `string`

Defined in: [ui/src/api-server/ai/openai-compatible.ts:161](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/openai-compatible.ts#L161)

Model used when a request does not name one.

#### Inherited from

[`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md).[`defaultModel`](../../openai-compatible/classes/OpenAiCompatibleProvider.md#defaultmodel)

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/openai-compatible.ts:160](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/openai-compatible.ts#L160)

Stable identifier, used in logs and in `AI_PROVIDER`.

#### Inherited from

[`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md).[`name`](../../openai-compatible/classes/OpenAiCompatibleProvider.md#name)

## Methods

### chat()

> **chat**(`request`): `Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

Defined in: [ui/src/api-server/ai/openai-compatible.ts:192](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/openai-compatible.ts#L192)

One-shot completion, for callers with nothing to stream to.

#### Parameters

##### request

[`AiChatRequest`](../../provider/type-aliases/AiChatRequest.md)

#### Returns

`Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

#### Inherited from

[`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md).[`chat`](../../openai-compatible/classes/OpenAiCompatibleProvider.md#chat)

***

### streamChat()

> **streamChat**(`request`): `AsyncIterable`\<[`AiProviderEvent`](../../provider/type-aliases/AiProviderEvent.md)\>

Defined in: [ui/src/api-server/ai/openai-compatible.ts:215](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/openai-compatible.ts#L215)

Incremental completion. Yields text as it arrives and terminates with a
single `final` frame carrying tool calls and usage.

#### Parameters

##### request

[`AiChatRequest`](../../provider/type-aliases/AiChatRequest.md)

#### Returns

`AsyncIterable`\<[`AiProviderEvent`](../../provider/type-aliases/AiProviderEvent.md)\>

#### Inherited from

[`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md).[`streamChat`](../../openai-compatible/classes/OpenAiCompatibleProvider.md#streamchat)
