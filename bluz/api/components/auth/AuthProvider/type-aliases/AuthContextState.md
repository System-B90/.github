[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/auth/AuthProvider](../index.md) / AuthContextState

# Type Alias: AuthContextState

> **AuthContextState** = `object`

Defined in: [ui/src/components/auth/AuthProvider.tsx:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/auth/AuthProvider.tsx#L26)

## Properties

### addMessageHandler

> **addMessageHandler**: (`handler`) => () => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/auth/AuthProvider.tsx#L31)

#### Parameters

##### handler

[`MessageHandlerType`](../../../SessionWs/type-aliases/MessageHandlerType.md)

#### Returns

() => `void`

***

### canEdit

> **canEdit**: `boolean`

Defined in: [ui/src/components/auth/AuthProvider.tsx:29](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/auth/AuthProvider.tsx#L29)

***

### degraded

> **degraded**: `boolean`

Defined in: [ui/src/components/auth/AuthProvider.tsx:30](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/auth/AuthProvider.tsx#L30)

***

### deregisterSyncObject

> **deregisterSyncObject**: (`syncObjectId`) => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:39](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/auth/AuthProvider.tsx#L39)

#### Parameters

##### syncObjectId

`string`

#### Returns

`void`

***

### logout

> **logout**: () => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/auth/AuthProvider.tsx#L28)

#### Returns

`void`

***

### registerSyncObject

> **registerSyncObject**: (`syncObjectId`) => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:38](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/auth/AuthProvider.tsx#L38)

Subscribe to a sync object for scoped broadcasts. Survives reconnects —
the transport replays every registered id on each new socket, so callers
must not try to re-register on their own (#525).

#### Parameters

##### syncObjectId

`string`

#### Returns

`void`

***

### sendMessage

> **sendMessage**: (`data`) => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:32](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/auth/AuthProvider.tsx#L32)

#### Parameters

##### data

[`WebSocketSessionMessage`](WebSocketSessionMessage.md)

#### Returns

`void`

***

### userData

> **userData**: `AuthSessionUser`

Defined in: [ui/src/components/auth/AuthProvider.tsx:27](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/auth/AuthProvider.tsx#L27)
