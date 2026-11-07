[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [components/SessionWs](../index.md) / useSessionWebSocketContext

# Function: useSessionWebSocketContext()

> **useSessionWebSocketContext**(): `object`

Defined in: [ui/src/components/SessionWs.tsx:35](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/SessionWs.tsx#L35)

Custom hook to establish and manage client-side WebSocket sessions.
Manages event listener registrations, session heartbeats, and auto-reconnection
with exponential backoff on close/error.

## Returns

`object`
