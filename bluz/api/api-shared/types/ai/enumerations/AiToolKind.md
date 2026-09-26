[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/ai](../index.md) / AiToolKind

# Enumeration: AiToolKind

Defined in: [ui/src/api-shared/types/ai.ts:50](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L50)

Whether running a tool changes stored data. Read tools run unattended;
write tools stop the turn and wait for the human to approve the exact call.

## Enumeration Members

### Prompt

> **Prompt**: `"prompt"`

Defined in: [ui/src/api-shared/types/ai.ts:58](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L58)

Not a data operation at all: the tool's whole effect is to put a
question to the human and stop the turn. Answered by the client, never
executed on the server.

***

### Read

> **Read**: `"read"`

Defined in: [ui/src/api-shared/types/ai.ts:51](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L51)

***

### Write

> **Write**: `"write"`

Defined in: [ui/src/api-shared/types/ai.ts:52](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/ai.ts#L52)
