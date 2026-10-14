[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/agent](../index.md) / AiAgentRunOptions

# Type Alias: AiAgentRunOptions

> **AiAgentRunOptions** = `object`

Defined in: [ui/src/api-server/ai/agent.ts:54](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/agent.ts#L54)

## Properties

### approvedToolCallIds

> **approvedToolCallIds**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/api-server/ai/agent.ts:60](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/agent.ts#L60)

Tool call ids the human approved for this turn.

***

### context

> **context**: [`AiToolContext`](../../tools/types/type-aliases/AiToolContext.md)

Defined in: [ui/src/api-server/ai/agent.ts:58](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/agent.ts#L58)

***

### messages

> **messages**: [`AiMessage`](../../../../api-shared/types/ai/type-aliases/AiMessage.md)[]

Defined in: [ui/src/api-server/ai/agent.ts:57](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/agent.ts#L57)

Transcript so far, excluding the system prompt.

***

### model?

> `optional` **model?**: `string`

Defined in: [ui/src/api-server/ai/agent.ts:63](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/agent.ts#L63)

***

### provider

> **provider**: [`AiProvider`](../../provider/type-aliases/AiProvider.md)

Defined in: [ui/src/api-server/ai/agent.ts:55](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/agent.ts#L55)

***

### registry?

> `optional` **registry?**: [`AiToolRegistry`](../../tools/type-aliases/AiToolRegistry.md)

Defined in: [ui/src/api-server/ai/agent.ts:62](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/agent.ts#L62)

Defaults to the live registry; the self-test passes fixture tools.

***

### seed?

> `optional` **seed?**: `number`

Defined in: [ui/src/api-server/ai/agent.ts:66](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/agent.ts#L66)

***

### signal?

> `optional` **signal?**: `AbortSignal`

Defined in: [ui/src/api-server/ai/agent.ts:67](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/agent.ts#L67)

***

### temperature?

> `optional` **temperature?**: `number`

Defined in: [ui/src/api-server/ai/agent.ts:65](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/ai/agent.ts#L65)

Sampling overrides; the self-test pins them so runs are comparable (#948).
