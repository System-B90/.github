[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/openai-compatible](../index.md) / OpenAiCompatibleProvider

# Class: OpenAiCompatibleProvider

Defined in: [ui/src/api-server/ai/openai-compatible.ts:172](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/openai-compatible.ts#L172)

## Extended by

- [`OpenAiProvider`](../../openai/classes/OpenAiProvider.md)
- [`OpenRouterProvider`](../../openrouter/classes/OpenRouterProvider.md)

## Implements

- [`AiProvider`](../../provider/type-aliases/AiProvider.md)

## Constructors

### Constructor

> **new OpenAiCompatibleProvider**(`options`): `OpenAiCompatibleProvider`

Defined in: [ui/src/api-server/ai/openai-compatible.ts:181](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/openai-compatible.ts#L181)

#### Parameters

##### options

###### apiKey

`string` \| [`AiKeySource`](../../key-source/type-aliases/AiKeySource.md)

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

Defined in: [ui/src/api-server/ai/openai-compatible.ts:175](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/openai-compatible.ts#L175)

Model used when a request does not name one.

#### Implementation of

`AiProvider.defaultModel`

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/openai-compatible.ts:174](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/openai-compatible.ts#L174)

Stable identifier, used in logs and in `AI_PROVIDER`.

#### Implementation of

`AiProvider.name`

## Methods

### chat()

> **chat**(`request`): `Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

Defined in: [ui/src/api-server/ai/openai-compatible.ts:208](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/openai-compatible.ts#L208)

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

Defined in: [ui/src/api-server/ai/openai-compatible.ts:308](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/openai-compatible.ts#L308)

`GET {baseUrl}/models`. With Open WebUI the base URL is `…/api`, so this
is its `/api/models`; OpenAI, OpenRouter and vLLM answer the same path.

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

Defined in: [ui/src/api-server/ai/openai-compatible.ts:233](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/openai-compatible.ts#L233)

Incremental completion. Yields text as it arrives and terminates with a
single `final` frame carrying tool calls and usage.

#### Parameters

##### request

[`AiChatRequest`](../../provider/type-aliases/AiChatRequest.md)

#### Returns

`AsyncIterable`\<[`AiProviderEvent`](../../provider/type-aliases/AiProviderEvent.md)\>

#### Implementation of

`AiProvider.streamChat`
