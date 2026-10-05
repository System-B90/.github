[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiChatRequest

# Type Alias: AiChatRequest

> **AiChatRequest** = `object`

Defined in: [ui/src/api-server/ai/provider.ts:23](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/provider.ts#L23)

Normalised request handed to a provider.

## Properties

### maxTokens?

> `optional` **maxTokens?**: `number`

Defined in: [ui/src/api-server/ai/provider.ts:28](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/provider.ts#L28)

***

### messages

> **messages**: [`AiMessage`](../../../../api-shared/types/ai/type-aliases/AiMessage.md)[]

Defined in: [ui/src/api-server/ai/provider.ts:24](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/provider.ts#L24)

***

### model?

> `optional` **model?**: `string`

Defined in: [ui/src/api-server/ai/provider.ts:26](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/provider.ts#L26)

***

### signal?

> `optional` **signal?**: `AbortSignal`

Defined in: [ui/src/api-server/ai/provider.ts:30](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/provider.ts#L30)

Aborts the upstream call when the browser disconnects.

***

### temperature?

> `optional` **temperature?**: `number`

Defined in: [ui/src/api-server/ai/provider.ts:27](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/provider.ts#L27)

***

### tools?

> `optional` **tools?**: [`AiToolSpec`](AiToolSpec.md)[]

Defined in: [ui/src/api-server/ai/provider.ts:25](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/provider.ts#L25)
