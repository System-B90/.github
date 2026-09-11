[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/UseEventActions](../index.md) / useEventActions

# Function: useEventActions()

> **useEventActions**(`events`, `offlineMode`, `captureEventBeforeEdit`, `dispatch`, `remoteDispatch`, `markEventCreatedLocally`): `object`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventActions.ts:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventActions.ts#L16)

## Parameters

### events

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[]

### offlineMode

`boolean`

### captureEventBeforeEdit

(`ev`) => `void`

### dispatch

(`action`) => `void`

### remoteDispatch

(`action`) => `void`

### markEventCreatedLocally

(`eventId`) => `void`

## Returns

`object`

### deleteEvent

> **deleteEvent**: (`eventId`, `initiator`) => `void`

#### Parameters

##### eventId

`string`

##### initiator?

[`EventChangeInitiator`](../../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md) = `EventChangeInitiator.EventDialog`

#### Returns

`void`

### saveEvent

> **saveEvent**: (`eventPartial`, `initiator`) => `void`

#### Parameters

##### eventPartial

`Partial`\<[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)\>

##### initiator?

[`EventChangeInitiator`](../../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md) = `EventChangeInitiator.EventDialog`

#### Returns

`void`

### syncHistoryTravel

> **syncHistoryTravel**: (`from`, `to`) => `void`

#### Parameters

##### from

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[]

##### to

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[]

#### Returns

`void`
