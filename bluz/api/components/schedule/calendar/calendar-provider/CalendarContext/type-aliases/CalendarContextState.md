[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/CalendarContext](../index.md) / CalendarContextState

# Type Alias: CalendarContextState

> **CalendarContextState** = `object`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:16](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L16)

## Properties

### deleteEvent

> **deleteEvent**: (`eventId`, `initiator?`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:47](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L47)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

##### initiator?

[`EventChangeInitiator`](../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

#### Returns

`void`

***

### deleteEvents

> **deleteEvents**: (`eventIds`, `initiator?`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:50](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L50)

#### Parameters

##### eventIds

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)[]

##### initiator?

[`EventChangeInitiator`](../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

#### Returns

`void`

***

### dispatch

> **dispatch**: (`action`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:53](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L53)

#### Parameters

##### action

[`CalendarAction`](../../hooks/UseEventState/type-aliases/CalendarAction.md)

#### Returns

`void`

***

### endDate

> **endDate**: `Date` \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:20](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L20)

***

### eventLocks

> **eventLocks**: `Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:33](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L33)

***

### events

> **events**: [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:18](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L18)

***

### isLoadingEvents

> **isLoadingEvents**: `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:30](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L30)

***

### isReadOnlyIteration

> **isReadOnlyIteration**: `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:26](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L26)

***

### iterationId

> **iterationId**: [`IterationId`](../../../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:24](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L24)

***

### lockEvent

> **lockEvent**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:56](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L56)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`

***

### redo

> **redo**: () => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:52](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L52)

#### Returns

`void`

***

### saveEvent

> **saveEvent**: (`event`, `initiator?`) => [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:46](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L46)

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

### saveEvents

> **saveEvents**: (`events`, `initiator?`) => [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:49](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L49)

Bulk forms of the above: one dispatch, one undo step, one request (#932).

#### Parameters

##### events

`Partial`\<[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)\>[]

##### initiator?

[`EventChangeInitiator`](../../../../../../api-shared/types/event-history/enumerations/EventChangeInitiator.md)

#### Returns

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

***

### setEndDate

> **setEndDate**: `Dispatch`\<`SetStateAction`\<`Date` \| `undefined`\>\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:37](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L37)

***

### setIterationId

> **setIterationId**: `Dispatch`\<`SetStateAction`\<[`IterationId`](../../../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`\>\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:38](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L38)

***

### setStartDate

> **setStartDate**: `Dispatch`\<`SetStateAction`\<`Date` \| `undefined`\>\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:36](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L36)

***

### startDate

> **startDate**: `Date` \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:19](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L19)

***

### undo

> **undo**: () => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:51](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L51)

#### Returns

`void`

***

### unlockEvent

> **unlockEvent**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:57](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L57)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`
