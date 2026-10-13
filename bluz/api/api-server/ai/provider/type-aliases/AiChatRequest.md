[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiChatRequest

# Type Alias: AiChatRequest

> **AiChatRequest** = `object`

Defined in: [ui/src/api-server/ai/provider.ts:23](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/ai/provider.ts#L23)

Normalised request handed to a provider.

## Properties

### maxTokens?

> `optional` **maxTokens?**: `number`

Defined in: [ui/src/api-server/ai/provider.ts:30](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/ai/provider.ts#L30)

***

### messages

> **messages**: [`AiMessage`](../../../../api-shared/types/ai/type-aliases/AiMessage.md)[]

Defined in: [ui/src/api-server/ai/provider.ts:24](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/ai/provider.ts#L24)

***

### model?

> `optional` **model?**: `string`

Defined in: [ui/src/api-server/ai/provider.ts:26](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/ai/provider.ts#L26)

***

### seed?

> `optional` **seed?**: `number`

Defined in: [ui/src/api-server/ai/provider.ts:29](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/ai/provider.ts#L29)

Best-effort determinism; providers that don't support it ignore it.

***

### signal?

> `optional` **signal?**: `AbortSignal`

Defined in: [ui/src/api-server/ai/provider.ts:32](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/ai/provider.ts#L32)

Aborts the upstream call when the browser disconnects.

***

### temperature?

> `optional` **temperature?**: `number`

Defined in: [ui/src/api-server/ai/provider.ts:27](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/ai/provider.ts#L27)

***

### tools?

> `optional` **tools?**: [`AiToolSpec`](AiToolSpec.md)[]

Defined in: [ui/src/api-server/ai/provider.ts:25](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/ai/provider.ts#L25)
