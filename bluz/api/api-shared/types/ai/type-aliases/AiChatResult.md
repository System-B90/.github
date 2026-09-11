[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiChatResult

# Type Alias: AiChatResult

> **AiChatResult** = `object`

Defined in: [ui/src/api-shared/types/ai.ts:94](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L94)

Non-streaming result. The streaming route is the default path, but the
provider interface also answers in one shot for server-side callers (jobs,
CLI) that have nothing to stream to.

## Properties

### content

> **content**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:95](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L95)

***

### finishReason?

> `optional` **finishReason?**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:100](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L100)

Why generation ended — e.g. `stop`, `tool_calls`, `length`.

***

### model

> **model**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:97](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L97)

***

### toolCalls?

> `optional` **toolCalls?**: [`AiToolCall`](AiToolCall.md)[]

Defined in: [ui/src/api-shared/types/ai.ts:96](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L96)

***

### usage?

> `optional` **usage?**: [`AiUsage`](AiUsage.md)

Defined in: [ui/src/api-shared/types/ai.ts:98](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L98)
