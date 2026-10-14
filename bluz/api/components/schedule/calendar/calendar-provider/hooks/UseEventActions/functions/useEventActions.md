[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/UseEventActions](../index.md) / useEventActions

# Function: useEventActions()

> **useEventActions**(`events`, `offlineMode`, `captureEventBeforeEdit`, `dispatch`, `remoteDispatch`, `markEventCreatedLocally`, `isEventCreatedLocally`, `iterationScope?`): `object`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventActions.ts:24](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventActions.ts#L24)

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

### deleteEvent

> **deleteEvent**: (`eventId`, `initiator`) => `void`

#### Parameters

##### eventId

`string`

##### initiator?

[`EventChangeInitiator`](../../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md) = `EventChangeInitiator.EventDialog`

#### Returns

`void`

### deleteEvents

> **deleteEvents**: (`eventIds`, `initiator`) => `void`

Bulk [deleteEvent](#useeventactions) (#932): one dispatch, one request, one snackbar.

#### Parameters

##### eventIds

`string`[]

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

### saveEvents

> **saveEvents**: (`eventPartials`, `initiator`) => [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[]

Bulk [saveEvent](#useeventactions) (#932): one state dispatch (so one undo step), at
most one create and one update request, and one summary snackbar. The
id→event lookup is built once rather than a `find` per event.

#### Parameters

##### eventPartials

`Partial`\<[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)\>[]

##### initiator?

[`EventChangeInitiator`](../../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md) = `EventChangeInitiator.EventDialog`

#### Returns

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[]

The events as applied locally; empty when refused.

### syncHistoryTravel

> **syncHistoryTravel**: (`from`, `to`) => `void`

#### Parameters

##### from

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[]

##### to

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[]

#### Returns

`void`
