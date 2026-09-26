[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/lock-state](../index.md) / toPublicLocks

# Function: toPublicLocks()

> **toPublicLocks**(`state`): `Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/lock-state.ts:130](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/lock-state.ts#L130)

Project the internal lock state down to the public map consumers read,
dropping the bookkeeping expiry timestamps.

## Parameters

### state

[`LockState`](../type-aliases/LockState.md)

The current lock state.

## Returns

`Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>

A map of event id → lock message.
