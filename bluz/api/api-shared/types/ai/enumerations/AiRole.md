[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiRole

# Enumeration: AiRole

Defined in: [ui/src/api-shared/types/ai.ts:11](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L11)

Who produced a message in a conversation.

## Enumeration Members

### Assistant

> **Assistant**: `"assistant"`

Defined in: [ui/src/api-shared/types/ai.ts:17](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L17)

Written by the model — may carry tool calls instead of text.

***

### System

> **System**: `"system"`

Defined in: [ui/src/api-shared/types/ai.ts:13](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L13)

Standing instructions. At most one, first in the list.

***

### Tool

> **Tool**: `"tool"`

Defined in: [ui/src/api-shared/types/ai.ts:19](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L19)

The result of running one tool the assistant asked for.

***

### User

> **User**: `"user"`

Defined in: [ui/src/api-shared/types/ai.ts:15](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L15)

Written by the human.
