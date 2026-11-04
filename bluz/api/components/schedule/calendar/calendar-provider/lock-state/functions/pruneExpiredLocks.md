[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/lock-state](../index.md) / pruneExpiredLocks

# Function: pruneExpiredLocks()

> **pruneExpiredLocks**(`state`, `now`): [`LockState`](../type-aliases/LockState.md)

Defined in: [ui/src/components/schedule/calendar/calendar-provider/lock-state.ts:113](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/calendar/calendar-provider/lock-state.ts#L113)

Remove every lock whose expiry has passed.

## Parameters

### state

[`LockState`](../type-aliases/LockState.md)

The current lock state.

### now

`number`

Current epoch time in ms.

## Returns

[`LockState`](../type-aliases/LockState.md)

A new state object, or the same reference when nothing expired.
