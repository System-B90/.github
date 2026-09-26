[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiChatResult

# Type Alias: AiChatResult

> **AiChatResult** = `object`

Defined in: [ui/src/api-shared/types/ai.ts:127](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L127)

Non-streaming result. The streaming route is the default path, but the
provider interface also answers in one shot for server-side callers (jobs,
CLI) that have nothing to stream to.

## Properties

### content

> **content**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:128](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L128)

***

### finishReason?

> `optional` **finishReason?**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:133](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L133)

Why generation ended — e.g. `stop`, `tool_calls`, `length`.

***

### model

> **model**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:130](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L130)

***

### toolCalls?

> `optional` **toolCalls?**: [`AiToolCall`](AiToolCall.md)[]

Defined in: [ui/src/api-shared/types/ai.ts:129](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L129)

***

### usage?

> `optional` **usage?**: [`AiUsage`](AiUsage.md)

Defined in: [ui/src/api-shared/types/ai.ts:131](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L131)
