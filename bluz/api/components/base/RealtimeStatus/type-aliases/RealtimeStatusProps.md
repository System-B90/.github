[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/RealtimeStatus](../index.md) / RealtimeStatusProps

# Type Alias: RealtimeStatusProps

> **RealtimeStatusProps** = `object`

Defined in: [ui/src/components/base/RealtimeStatus.tsx:16](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/RealtimeStatus.tsx#L16)

The socket ref owned by the single `useSessionWebSocketContext()` call in
`AuthProvider`. Passed down rather than re-invoked here: that hook *opens* a
connection, so calling it again would run a second socket in parallel.

## Properties

### ws

> **ws**: `ReturnType`\<*typeof* [`useSessionWebSocketContext`](../../../SessionWs/functions/useSessionWebSocketContext.md)\>\[`"ws"`\]

Defined in: [ui/src/components/base/RealtimeStatus.tsx:17](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/RealtimeStatus.tsx#L17)
