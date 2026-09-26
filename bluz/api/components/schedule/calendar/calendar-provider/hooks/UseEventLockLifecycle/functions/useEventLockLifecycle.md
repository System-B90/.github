[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/UseEventLockLifecycle](../index.md) / useEventLockLifecycle

# Function: useEventLockLifecycle()

> **useEventLockLifecycle**(`openId`, `lockEvent`, `unlockEvent`): `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventLockLifecycle.ts:20](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventLockLifecycle.ts#L20)

Holds an event lock for as long as its dialog is open.

Broadcasts a lock when a dialog opens on an existing event, re-emits it on a
heartbeat so other clients keep seeing it (and clients that connected later
learn about it), and releases it when the dialog closes or the page goes
away. The held id is tracked in a ref so the matching unlock fires however
the dialog was opened or closed.

## Parameters

### openId

`string` \| `null`

The event whose dialog is open, or `null` when none is.

### lockEvent

(`eventId`) => `void`

Broadcasts a lock for an event.

### unlockEvent

(`eventId`) => `void`

Releases the lock on an event.

## Returns

`void`
