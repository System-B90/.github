[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/provider](../index.md) / AiChatRequest

# Type Alias: AiChatRequest

> **AiChatRequest** = `object`

Defined in: [ui/src/api-server/ai/provider.ts:22](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L22)

Normalised request handed to a provider.

## Properties

### maxTokens?

> `optional` **maxTokens?**: `number`

Defined in: [ui/src/api-server/ai/provider.ts:27](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L27)

***

### messages

> **messages**: [`AiMessage`](../../../../api-shared/types/ai/type-aliases/AiMessage.md)[]

Defined in: [ui/src/api-server/ai/provider.ts:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L23)

***

### model?

> `optional` **model?**: `string`

Defined in: [ui/src/api-server/ai/provider.ts:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L25)

***

### signal?

> `optional` **signal?**: `AbortSignal`

Defined in: [ui/src/api-server/ai/provider.ts:29](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L29)

Aborts the upstream call when the browser disconnects.

***

### temperature?

> `optional` **temperature?**: `number`

Defined in: [ui/src/api-server/ai/provider.ts:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L26)

***

### tools?

> `optional` **tools?**: [`AiToolSpec`](AiToolSpec.md)[]

Defined in: [ui/src/api-server/ai/provider.ts:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/ai/provider.ts#L24)
