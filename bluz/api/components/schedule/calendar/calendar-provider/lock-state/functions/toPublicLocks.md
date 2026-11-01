[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/lock-state](../index.md) / toPublicLocks

# Function: toPublicLocks()

> **toPublicLocks**(`state`): `Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/lock-state.ts:140](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/schedule/calendar/calendar-provider/lock-state.ts#L140)

Project the internal lock state down to the public map consumers read,
dropping the bookkeeping expiry timestamps.

## Parameters

### state

[`LockState`](../type-aliases/LockState.md)

The current lock state.

## Returns

`Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>

A map of event id → lock message.
