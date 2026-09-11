[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiStreamEventType

# Enumeration: AiStreamEventType

Defined in: [ui/src/api-shared/types/ai.ts:103](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L103)

## Enumeration Members

### Delta

> **Delta**: `"delta"`

Defined in: [ui/src/api-shared/types/ai.ts:105](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L105)

A fragment of the assistant's visible answer.

***

### Done

> **Done**: `"done"`

Defined in: [ui/src/api-shared/types/ai.ts:113](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L113)

Terminal success frame.

***

### Error

> **Error**: `"error"`

Defined in: [ui/src/api-shared/types/ai.ts:115](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L115)

Terminal failure frame.

***

### ToolProposal

> **ToolProposal**: `"tool_proposal"`

Defined in: [ui/src/api-shared/types/ai.ts:111](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L111)

A write tool needs the human to approve it before it runs.

***

### ToolResult

> **ToolResult**: `"tool_result"`

Defined in: [ui/src/api-shared/types/ai.ts:109](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L109)

A read tool finished; carries a short human-readable summary.

***

### ToolStart

> **ToolStart**: `"tool_start"`

Defined in: [ui/src/api-shared/types/ai.ts:107](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/ai.ts#L107)

A read tool started running.
