[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/CalendarContext](../index.md) / CalendarContextState

# Type Alias: CalendarContextState

> **CalendarContextState** = `object`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:11](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L11)

## Properties

### deleteEvent

> **deleteEvent**: (`eventId`, `initiator?`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:42](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L42)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

##### initiator?

[`EventChangeInitiator`](../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

#### Returns

`void`

***

### dispatch

> **dispatch**: (`action`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:45](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L45)

#### Parameters

##### action

[`CalendarAction`](../../hooks/UseEventState/type-aliases/CalendarAction.md)

#### Returns

`void`

***

### endDate

> **endDate**: `Date` \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:15](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L15)

***

### eventLocks

> **eventLocks**: `Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:28](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L28)

***

### events

> **events**: [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:13](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L13)

***

### isLoadingEvents

> **isLoadingEvents**: `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L25)

***

### isReadOnlyIteration

> **isReadOnlyIteration**: `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:21](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L21)

***

### iterationId

> **iterationId**: [`IterationId`](../../../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:19](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L19)

***

### lockEvent

> **lockEvent**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:48](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L48)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`

***

### redo

> **redo**: () => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:44](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L44)

#### Returns

`void`

***

### saveEvent

> **saveEvent**: (`event`, `initiator?`) => [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:41](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L41)

Persists an event. `initiator` names the user action behind the write so
the server can log it (see api-shared/types/event-history.ts); it
defaults to an event-dialog edit.

#### Parameters

##### event

`Partial`\<[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)\>

##### initiator?

[`EventChangeInitiator`](../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

#### Returns

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `undefined`

***

### setEndDate

> **setEndDate**: `Dispatch`\<`SetStateAction`\<`Date` \| `undefined`\>\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:32](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L32)

***

### setIterationId

> **setIterationId**: `Dispatch`\<`SetStateAction`\<[`IterationId`](../../../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`\>\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:33](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L33)

***

### setStartDate

> **setStartDate**: `Dispatch`\<`SetStateAction`\<`Date` \| `undefined`\>\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L31)

***

### startDate

> **startDate**: `Date` \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:14](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L14)

***

### undo

> **undo**: () => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:43](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L43)

#### Returns

`void`

***

### unlockEvent

> **unlockEvent**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:49](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L49)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`
