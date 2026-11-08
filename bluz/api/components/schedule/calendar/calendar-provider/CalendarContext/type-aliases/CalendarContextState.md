[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/CalendarContext](../index.md) / CalendarContextState

# Type Alias: CalendarContextState

> **CalendarContextState** = `object`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:30](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L30)

## Properties

### closeSnapshotView

> **closeSnapshotView**: () => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:49](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L49)

Back to the live schedule.

#### Returns

`void`

***

### deleteEvent

> **deleteEvent**: (`eventId`, `initiator?`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:70](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L70)

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

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:73](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L73)

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

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:76](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L76)

#### Parameters

##### action

[`CalendarAction`](../../hooks/UseEventState/type-aliases/CalendarAction.md)

#### Returns

`void`

***

### endDate

> **endDate**: `Date` \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:34](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L34)

***

### eventLocks

> **eventLocks**: `Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md)\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:56](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L56)

***

### events

> **events**: [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:32](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L32)

***

### isLoadingEvents

> **isLoadingEvents**: `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:53](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L53)

***

### isReadOnlyIteration

> **isReadOnlyIteration**: `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:42](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L42)

***

### iterationId

> **iterationId**: [`IterationId`](../../../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:38](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L38)

***

### lockEvent

> **lockEvent**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:85](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L85)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`

***

### openSnapshotView

> **openSnapshotView**: (`snapshotId`) => `Promise`\<[`SnapshotView`](SnapshotView.md)\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:47](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L47)

Shows a snapshot read-only, moving the view to its range.

#### Parameters

##### snapshotId

`string`

#### Returns

`Promise`\<[`SnapshotView`](SnapshotView.md)\>

***

### redo

> **redo**: () => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:75](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L75)

#### Returns

`void`

***

### reloadEvents

> **reloadEvents**: () => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:82](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L82)

Refetches the shown range from the server as a remote change: it
replaces local state without becoming an undo step. For server-side
bulk writes (snapshot restore) that the user must not "undo" locally.

#### Returns

`void`

***

### saveEvent

> **saveEvent**: (`event`, `initiator?`) => [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:69](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L69)

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

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:72](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L72)

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

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:60](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L60)

***

### setIterationId

> **setIterationId**: `Dispatch`\<`SetStateAction`\<[`IterationId`](../../../../../../api-shared/types/iteration/type-aliases/IterationId.md) \| `undefined`\>\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:61](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L61)

***

### setStartDate

> **setStartDate**: `Dispatch`\<`SetStateAction`\<`Date` \| `undefined`\>\>

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:59](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L59)

***

### snapshotView

> **snapshotView**: `null` \| [`SnapshotView`](SnapshotView.md)

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:45](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L45)

***

### startDate

> **startDate**: `Date` \| `undefined`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:33](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L33)

***

### undo

> **undo**: () => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:74](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L74)

#### Returns

`void`

***

### unlockEvent

> **unlockEvent**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx:86](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar-provider/CalendarContext.tsx#L86)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

#### Returns

`void`
