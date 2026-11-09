[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/auth/AuthProvider](../index.md) / AuthContextState

# Type Alias: AuthContextState

> **AuthContextState** = `object`

Defined in: [ui/src/components/auth/AuthProvider.tsx:28](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/auth/AuthProvider.tsx#L28)

## Properties

### addMessageHandler

> **addMessageHandler**: (`handler`) => () => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:35](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/auth/AuthProvider.tsx#L35)

#### Parameters

##### handler

[`MessageHandlerType`](../../../SessionWs/type-aliases/MessageHandlerType.md)

#### Returns

() => `void`

***

### canEdit

> **canEdit**: `boolean`

Defined in: [ui/src/components/auth/AuthProvider.tsx:31](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/auth/AuthProvider.tsx#L31)

***

### degraded

> **degraded**: `boolean`

Defined in: [ui/src/components/auth/AuthProvider.tsx:34](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/auth/AuthProvider.tsx#L34)

***

### deregisterSyncObject

> **deregisterSyncObject**: (`syncObjectId`) => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:43](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/auth/AuthProvider.tsx#L43)

#### Parameters

##### syncObjectId

`string`

#### Returns

`void`

***

### isReadOnlyUser

> **isReadOnlyUser**: `boolean`

Defined in: [ui/src/components/auth/AuthProvider.tsx:33](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/auth/AuthProvider.tsx#L33)

Checker clearance: may view the schedule, never write or open the gantt.

***

### logout

> **logout**: () => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:30](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/auth/AuthProvider.tsx#L30)

#### Returns

`void`

***

### registerSyncObject

> **registerSyncObject**: (`syncObjectId`) => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:42](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/auth/AuthProvider.tsx#L42)

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

Defined in: [ui/src/components/auth/AuthProvider.tsx:36](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/auth/AuthProvider.tsx#L36)

#### Parameters

##### data

[`WebSocketSessionMessage`](WebSocketSessionMessage.md)

#### Returns

`void`

***

### userData

> **userData**: `AuthSessionUser`

Defined in: [ui/src/components/auth/AuthProvider.tsx:29](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/auth/AuthProvider.tsx#L29)
