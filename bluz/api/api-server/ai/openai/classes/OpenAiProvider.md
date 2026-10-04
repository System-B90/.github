[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/openai](../index.md) / OpenAiProvider

# Class: OpenAiProvider

Defined in: [ui/src/api-server/ai/openai.ts:16](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/openai.ts#L16)

## Extends

- [`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md)

## Constructors

### Constructor

> **new OpenAiProvider**(`options`): `OpenAiProvider`

Defined in: [ui/src/api-server/ai/openai.ts:17](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/openai.ts#L17)

#### Parameters

##### options

###### apiKey

`string`

###### baseUrl

`string`

###### defaultModel

`string`

#### Returns

`OpenAiProvider`

#### Overrides

[`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md).[`constructor`](../../openai-compatible/classes/OpenAiCompatibleProvider.md#constructor)

## Properties

### defaultModel

> `readonly` **defaultModel**: `string`

Defined in: [ui/src/api-server/ai/openai-compatible.ts:163](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/openai-compatible.ts#L163)

Model used when a request does not name one.

#### Inherited from

[`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md).[`defaultModel`](../../openai-compatible/classes/OpenAiCompatibleProvider.md#defaultmodel)

***

### name

> `readonly` **name**: `string`

Defined in: [ui/src/api-server/ai/openai-compatible.ts:162](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/openai-compatible.ts#L162)

Stable identifier, used in logs and in `AI_PROVIDER`.

#### Inherited from

[`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md).[`name`](../../openai-compatible/classes/OpenAiCompatibleProvider.md#name)

## Methods

### chat()

> **chat**(`request`): `Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

Defined in: [ui/src/api-server/ai/openai-compatible.ts:194](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/openai-compatible.ts#L194)

One-shot completion, for callers with nothing to stream to.

#### Parameters

##### request

[`AiChatRequest`](../../provider/type-aliases/AiChatRequest.md)

#### Returns

`Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

#### Inherited from

[`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md).[`chat`](../../openai-compatible/classes/OpenAiCompatibleProvider.md#chat)

***

### listModels()

> **listModels**(`signal?`): `Promise`\<[`AiModelInfo`](../../../../api-shared/types/ai-models/type-aliases/AiModelInfo.md)[]\>

Defined in: [ui/src/api-server/ai/openai-compatible.ts:283](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/openai-compatible.ts#L283)

`GET {baseUrl}/models`. With Open WebUI the base URL is `…/api`, so this
is its `/api/models`; OpenAI, OpenRouter and vLLM answer the same path.

#### Parameters

##### signal?

`AbortSignal`

#### Returns

`Promise`\<[`AiModelInfo`](../../../../api-shared/types/ai-models/type-aliases/AiModelInfo.md)[]\>

#### Inherited from

[`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md).[`listModels`](../../openai-compatible/classes/OpenAiCompatibleProvider.md#listmodels)

***

### streamChat()

> **streamChat**(`request`): `AsyncIterable`\<[`AiProviderEvent`](../../provider/type-aliases/AiProviderEvent.md)\>

Defined in: [ui/src/api-server/ai/openai-compatible.ts:217](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/openai-compatible.ts#L217)

Incremental completion. Yields text as it arrives and terminates with a
single `final` frame carrying tool calls and usage.

#### Parameters

##### request

[`AiChatRequest`](../../provider/type-aliases/AiChatRequest.md)

#### Returns

`AsyncIterable`\<[`AiProviderEvent`](../../provider/type-aliases/AiProviderEvent.md)\>

#### Inherited from

[`OpenAiCompatibleProvider`](../../openai-compatible/classes/OpenAiCompatibleProvider.md).[`streamChat`](../../openai-compatible/classes/OpenAiCompatibleProvider.md#streamchat)
