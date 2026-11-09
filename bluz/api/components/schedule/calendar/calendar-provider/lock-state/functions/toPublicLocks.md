[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/lock-state](../index.md) / toPublicLocks

# Function: toPublicLocks()

> **toPublicLocks**(`state`): `Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/lock-state.ts:140](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/calendar/calendar-provider/lock-state.ts#L140)

Project the internal lock state down to the public map consumers read,
dropping the bookkeeping expiry timestamps.

## Parameters

### state

[`LockState`](../type-aliases/LockState.md)

The current lock state.

## Returns

`Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>

A map of event id → lock message.
