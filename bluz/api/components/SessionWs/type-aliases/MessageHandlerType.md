[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [components/SessionWs](../index.md) / MessageHandlerType

# Type Alias: MessageHandlerType

> **MessageHandlerType** = `SharedMessageHandlerType`\<[`MessageTypes`](../../../settings/enumerations/MessageTypes.md)\>

Defined in: [ui/src/components/SessionWs.tsx:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/SessionWs.tsx#L28)

Handler callback for processing incoming WebSocket messages on the client.

## Param

**messageType**

The type of WS message (from MessageTypes).

## Param

**data**

The JSON data payload containing domain entities/changes.

## Example

```typescript
const onWebSocketMessage: MessageHandlerType = (type, data) => {
  if (type === MessageTypes.COURSES_UPDATE) {
    loadCourses();
  }
};
```
