[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/lock-state](../index.md) / toStablePublicLocks

# Function: toStablePublicLocks()

> **toStablePublicLocks**(`previous`, `state`): `Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/lock-state.ts:146](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/schedule/calendar/calendar-provider/lock-state.ts#L146)

[toPublicLocks](toPublicLocks.md), but returns `previous` itself when every event still
has the same holder. A heartbeat only moves `expiresAt`, so without this
each one handed every calendar consumer a fresh map and re-rendered the
whole grid every [LOCK\_HEARTBEAT\_MS](../variables/LOCK_HEARTBEAT_MS.md) per remote editor (#922).

## Parameters

### previous

`Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>

### state

[`LockState`](../type-aliases/LockState.md)

## Returns

`Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>
