[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/openrouter](../index.md) / OpenRouterProvider

# Class: OpenRouterProvider

Defined in: [ui/src/api-server/ai/openrouter.ts:147](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/openrouter.ts#L147)

## Implements

- [`AiProvider`](../../provider/type-aliases/AiProvider.md)

## Constructors

### Constructor

> **new OpenRouterProvider**(`options`): `OpenRouterProvider`

Defined in: [ui/src/api-server/ai/openrouter.ts:157](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/openrouter.ts#L157)

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

###### title?

`string`

#### Returns

`OpenRouterProvider`

## Properties

### defaultModel

> `readonly` **defaultModel**: `string`

Defined in: [ui/src/api-server/ai/openrouter.ts:149](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/openrouter.ts#L149)

Model used when a request does not name one.

#### Implementation of

`AiProvider.defaultModel`

***

### name

> `readonly` **name**: `"openrouter"` = `"openrouter"`

Defined in: [ui/src/api-server/ai/openrouter.ts:148](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/openrouter.ts#L148)

Stable identifier, used in logs and in `AI_PROVIDER`.

#### Implementation of

`AiProvider.name`

## Methods

### chat()

> **chat**(`request`): `Promise`\<[`AiChatResult`](../../../../api-shared/types/ai/type-aliases/AiChatResult.md)\>

Defined in: [ui/src/api-server/ai/openrouter.ts:176](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/openrouter.ts#L176)

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

Defined in: [ui/src/api-server/ai/openrouter.ts:199](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/openrouter.ts#L199)

Incremental completion. Yields text as it arrives and terminates with a
single `final` frame carrying tool calls and usage.

#### Parameters

##### request

[`AiChatRequest`](../../provider/type-aliases/AiChatRequest.md)

#### Returns

`AsyncIterable`\<[`AiProviderEvent`](../../provider/type-aliases/AiProviderEvent.md)\>

#### Implementation of

`AiProvider.streamChat`
