[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [components/SessionWs](../index.md) / MessageHandlerType

# Type Alias: MessageHandlerType

> **MessageHandlerType** = `SharedMessageHandlerType`\<[`MessageTypes`](../../../settings/enumerations/MessageTypes.md)\>

Defined in: [ui/src/components/SessionWs.tsx:28](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/SessionWs.tsx#L28)

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
