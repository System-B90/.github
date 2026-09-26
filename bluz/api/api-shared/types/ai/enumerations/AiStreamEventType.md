[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiStreamEventType

# Enumeration: AiStreamEventType

Defined in: [ui/src/api-shared/types/ai.ts:136](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L136)

## Enumeration Members

### Choice

> **Choice**: `"choice"`

Defined in: [ui/src/api-shared/types/ai.ts:150](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L150)

The model is asking the human to pick between options.

***

### Delta

> **Delta**: `"delta"`

Defined in: [ui/src/api-shared/types/ai.ts:138](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L138)

A fragment of the assistant's visible answer.

***

### Done

> **Done**: `"done"`

Defined in: [ui/src/api-shared/types/ai.ts:158](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L158)

Terminal success frame.

***

### Error

> **Error**: `"error"`

Defined in: [ui/src/api-shared/types/ai.ts:160](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L160)

Terminal failure frame.

***

### Reasoning

> **Reasoning**: `"reasoning"`

Defined in: [ui/src/api-shared/types/ai.ts:143](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L143)

A fragment of the model's private reasoning. Rendered collapsed: it is
what makes an answer trustworthy, and noise the rest of the time.

***

### ReasoningDelta

> **ReasoningDelta**: `"reasoning_delta"`

Defined in: [ui/src/api-shared/types/ai.ts:148](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L148)

A fragment of a reasoning model's chain-of-thought, sent on a wire
channel separate from the visible answer. Shown collapsed by default.

***

### ToolProposal

> **ToolProposal**: `"tool_proposal"`

Defined in: [ui/src/api-shared/types/ai.ts:156](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L156)

A write tool needs the human to approve it before it runs.

***

### ToolResult

> **ToolResult**: `"tool_result"`

Defined in: [ui/src/api-shared/types/ai.ts:154](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L154)

A read tool finished; carries a short human-readable summary.

***

### ToolStart

> **ToolStart**: `"tool_start"`

Defined in: [ui/src/api-shared/types/ai.ts:152](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L152)

A read tool started running.
