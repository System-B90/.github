[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/auth/AuthProvider](../index.md) / AuthContextState

# Type Alias: AuthContextState

> **AuthContextState** = `object`

Defined in: [ui/src/components/auth/AuthProvider.tsx:28](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/auth/AuthProvider.tsx#L28)

## Properties

### addMessageHandler

> **addMessageHandler**: (`handler`) => () => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:37](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/auth/AuthProvider.tsx#L37)

#### Parameters

##### handler

[`MessageHandlerType`](../../../SessionWs/type-aliases/MessageHandlerType.md)

#### Returns

() => `void`

***

### breakGlass

> **breakGlass**: `boolean`

Defined in: [ui/src/components/auth/AuthProvider.tsx:36](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/auth/AuthProvider.tsx#L36)

Signed in with the break-glass user while Hive is offline: no Hive data.

***

### canEdit

> **canEdit**: `boolean`

Defined in: [ui/src/components/auth/AuthProvider.tsx:31](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/auth/AuthProvider.tsx#L31)

***

### degraded

> **degraded**: `boolean`

Defined in: [ui/src/components/auth/AuthProvider.tsx:34](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/auth/AuthProvider.tsx#L34)

***

### deregisterSyncObject

> **deregisterSyncObject**: (`syncObjectId`) => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:45](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/auth/AuthProvider.tsx#L45)

#### Parameters

##### syncObjectId

`string`

#### Returns

`void`

***

### isReadOnlyUser

> **isReadOnlyUser**: `boolean`

Defined in: [ui/src/components/auth/AuthProvider.tsx:33](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/auth/AuthProvider.tsx#L33)

Checker clearance: may view the schedule, never write or open the gantt.

***

### logout

> **logout**: () => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:30](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/auth/AuthProvider.tsx#L30)

#### Returns

`void`

***

### registerSyncObject

> **registerSyncObject**: (`syncObjectId`) => `void`

Defined in: [ui/src/components/auth/AuthProvider.tsx:44](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/auth/AuthProvider.tsx#L44)

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

Defined in: [ui/src/components/auth/AuthProvider.tsx:38](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/auth/AuthProvider.tsx#L38)

#### Parameters

##### data

[`WebSocketSessionMessage`](WebSocketSessionMessage.md)

#### Returns

`void`

***

### userData

> **userData**: `AuthSessionUser`

Defined in: [ui/src/components/auth/AuthProvider.tsx:29](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/auth/AuthProvider.tsx#L29)
