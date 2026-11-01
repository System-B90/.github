[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/UseEventState](../index.md) / useEventState

# Function: useEventState()

> **useEventState**(`initialState?`, `onTravel?`): `object`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts:274](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts#L274)

## Parameters

### initialState?

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[] = `[]`

### onTravel?

(`from`, `to`) => `void`

## Returns

`object`

### dispatch

> **dispatch**: (`action`) => `void`

#### Parameters

##### action

[`CalendarAction`](../type-aliases/CalendarAction.md)

#### Returns

`void`

### events

> **events**: [`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)[] = `history.present`

### redo

> **redo**: () => [`TravelOutcome`](../type-aliases/TravelOutcome.md)

#### Returns

[`TravelOutcome`](../type-aliases/TravelOutcome.md)

### remoteDispatch

> **remoteDispatch**: (`action`) => `void`

#### Parameters

##### action

[`CalendarAction`](../type-aliases/CalendarAction.md)

#### Returns

`void`

### undo

> **undo**: () => [`TravelOutcome`](../type-aliases/TravelOutcome.md)

#### Returns

[`TravelOutcome`](../type-aliases/TravelOutcome.md)

### undoDeletion

> **undoDeletion**: (`ids`) => `"stale"` \| [`TravelOutcome`](../type-aliases/TravelOutcome.md)

#### Parameters

##### ids

`string`[]

#### Returns

`"stale"` \| [`TravelOutcome`](../type-aliases/TravelOutcome.md)
