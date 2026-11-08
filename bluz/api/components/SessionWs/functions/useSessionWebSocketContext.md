[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [components/SessionWs](../index.md) / useSessionWebSocketContext

# Function: useSessionWebSocketContext()

> **useSessionWebSocketContext**(): `object`

Defined in: [ui/src/components/SessionWs.tsx:35](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/SessionWs.tsx#L35)

Custom hook to establish and manage client-side WebSocket sessions.
Manages event listener registrations, session heartbeats, and auto-reconnection
with exponential backoff on close/error.

## Returns

`object`
