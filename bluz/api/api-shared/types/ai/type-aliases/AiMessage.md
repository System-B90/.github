[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiMessage

# Type Alias: AiMessage

> **AiMessage** = `object`

Defined in: [ui/src/api-shared/types/ai.ts:34](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L34)

## Properties

### content

> **content**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:37](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L37)

Empty on an assistant turn that only requested tools.

***

### name?

> `optional` **name?**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:43](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L43)

Tool turns only, for rendering the transcript.

***

### role

> **role**: [`AiRole`](../enumerations/AiRole.md)

Defined in: [ui/src/api-shared/types/ai.ts:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L35)

***

### toolCallId?

> `optional` **toolCallId?**: `string`

Defined in: [ui/src/api-shared/types/ai.ts:41](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L41)

Tool turns only — which call this answers.

***

### toolCalls?

> `optional` **toolCalls?**: [`AiToolCall`](AiToolCall.md)[]

Defined in: [ui/src/api-shared/types/ai.ts:39](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L39)

Assistant turns only.
