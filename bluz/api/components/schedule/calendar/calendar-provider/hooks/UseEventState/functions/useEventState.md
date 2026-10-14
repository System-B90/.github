[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/UseEventState](../index.md) / useEventState

# Function: useEventState()

> **useEventState**(`initialState?`, `onTravel?`): `object`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts:247](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts#L247)

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

> **redo**: () => `void`

#### Returns

`void`

### remoteDispatch

> **remoteDispatch**: (`action`) => `void`

#### Parameters

##### action

[`CalendarAction`](../type-aliases/CalendarAction.md)

#### Returns

`void`

### undo

> **undo**: () => `void`

#### Returns

`void`
