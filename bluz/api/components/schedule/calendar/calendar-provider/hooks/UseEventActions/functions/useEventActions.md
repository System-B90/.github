[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/UseEventActions](../index.md) / useEventActions

# Function: useEventActions()

> **useEventActions**(`events`, `offlineMode`, `captureEventBeforeEdit`, `dispatch`, `remoteDispatch`, `markEventCreatedLocally`, `isEventCreatedLocally`, `iterationScope?`): `object`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventActions.ts:21](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventActions.ts#L21)

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

### isEventCreatedLocally

(`eventId`) => `boolean`

### iterationScope?

#### isReadOnlyIteration

`boolean`

#### iterationId?

`string`

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

> **saveEvent**: (`eventPartial`, `initiator`) => [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md) \| `undefined`

#### Parameters

##### eventPartial

`Partial`\<[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)\>

##### initiator?

[`EventChangeInitiator`](../../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md) = `EventChangeInitiator.EventDialog`

#### Returns

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md) \| `undefined`

### syncHistoryTravel

> **syncHistoryTravel**: (`from`, `to`) => `void`

#### Parameters

##### from

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[]

##### to

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[]

#### Returns

`void`
