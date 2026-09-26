[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/openai-compatible](../index.md) / OpenAiCompatibleProvider

# Class: OpenAiCompatibleProvider

Defined in: [ui/src/api-server/ai/openai-compatible.ts:159](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/openai-compatible.ts#L159)

## Extended by

- [`OpenAiProvider`](../../openai/classes/OpenAiProvider.md)
- [`OpenRouterProvider`](../../openrouter/classes/OpenRouterProvider.md)

## Implements

- [`AiProvider`](../../provider/type-aliases/AiProvider.md)

## Constructors

### Constructor

> **new OpenAiCompatibleProvider**(`options`): `OpenAiCompatibleProvider`

Defined in: [ui/src/api-server/ai/openai-compatible.ts:167](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/openai-compatible.ts#L167)

#### Parameters

##### options

###### apiKey

`string`

###### baseUrl

`string`

###### defaultModel

`string`

###### extraHeaders?

`Record`\<`string`, `string` \| `undefined`\>

e.g. OpenRouter's attribution headers. Omitted entries are skipped.

###### missingKeyMessage

`string`

Error shown when `apiKey` is empty — names the env var operators set.

###### name

`string`

Identifier reported in logs/`AI_PROVIDER` (e.g. "openrouter", "openai").

#### Returns

`OpenAiCompatibleProvider`

## Properties

### defaultModel

> `readonly` **defaultModel**: `string`

Defined in: [ui/src/api-server/ai/openai-compatible.ts:161](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/openai-compatible.ts#L161)

Model used when a request does not name one.

#### Implementation of

`AiProvider.defaultModel`

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/openai-compatible.ts:160](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/openai-compatible.ts#L160)

Stable identifier, used in logs and in `AI_PROVIDER`.

#### Implementation of

`AiProvider.name`

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

#### Implementation of

`AiProvider.chat`

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

#### Implementation of

`AiProvider.streamChat`
