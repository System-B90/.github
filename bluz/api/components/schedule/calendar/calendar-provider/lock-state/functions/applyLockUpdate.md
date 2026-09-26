[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/lock-state](../index.md) / applyLockUpdate

# Function: applyLockUpdate()

> **applyLockUpdate**(`state`, `eventId`, `lock`, `options`, `unlockedById?`): [`LockState`](../type-aliases/LockState.md)

Defined in: [ui/src/components/schedule/calendar/calendar-provider/lock-state.ts:70](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/lock-state.ts#L70)

Apply a single lock or unlock update to the lock state.

## Parameters

### state

[`LockState`](../type-aliases/LockState.md)

The current lock state.

### eventId

`string`

The event the update concerns.

### lock

[`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md) \| `null`

The incoming lock, or `null` to release the lock.

### options

`ApplyLockOptions`

Self id (for echo filtering), current time, and TTL.

### unlockedById?

`string`

When `lock` is `null`, the id of the client that sent
  the unlock. A stale or superseding unlock — one whose sender does not
  match who the tracked lock says currently holds it — is ignored instead
  of clearing a lock some other, later holder is still holding (#689).

## Returns

[`LockState`](../type-aliases/LockState.md)

A new state object, or the same reference when nothing changed.
