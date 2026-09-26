[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/agent](../index.md) / AiAgentRunOptions

# Type Alias: AiAgentRunOptions

> **AiAgentRunOptions** = `object`

Defined in: [ui/src/api-server/ai/agent.ts:54](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/agent.ts#L54)

## Properties

### approvedToolCallIds

> **approvedToolCallIds**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/api-server/ai/agent.ts:60](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/agent.ts#L60)

Tool call ids the human approved for this turn.

***

### context

> **context**: [`AiToolContext`](../../tools/types/type-aliases/AiToolContext.md)

Defined in: [ui/src/api-server/ai/agent.ts:58](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/agent.ts#L58)

***

### messages

> **messages**: [`AiMessage`](../../../../api-shared/types/ai/type-aliases/AiMessage.md)[]

Defined in: [ui/src/api-server/ai/agent.ts:57](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/agent.ts#L57)

Transcript so far, excluding the system prompt.

***

### model?

> `optional` **model?**: `string`

Defined in: [ui/src/api-server/ai/agent.ts:63](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/agent.ts#L63)

***

### provider

> **provider**: [`AiProvider`](../../provider/type-aliases/AiProvider.md)

Defined in: [ui/src/api-server/ai/agent.ts:55](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/agent.ts#L55)

***

### registry?

> `optional` **registry?**: [`AiToolRegistry`](../../tools/type-aliases/AiToolRegistry.md)

Defined in: [ui/src/api-server/ai/agent.ts:62](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/agent.ts#L62)

Defaults to the live registry; the self-test passes fixture tools.

***

### signal?

> `optional` **signal?**: `AbortSignal`

Defined in: [ui/src/api-server/ai/agent.ts:64](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/agent.ts#L64)
