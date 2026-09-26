[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/UseCalendarHandlers](../index.md) / useCalendarHandlers

# Function: useCalendarHandlers()

> **useCalendarHandlers**(`events`, `handleSaveEvent`, `handleDeleteEvent`, `setSelectedEvent`, `setOpenEventDialog`): `object`

Defined in: [ui/src/components/schedule/calendar/calendar/UseCalendarHandlers.ts:39](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/UseCalendarHandlers.ts#L39)

Custom React hook to manage calendar event logic, user interactions (e.g. drag & drop, select, click),
and keyboard shortcuts (copy, paste, delete).

## Parameters

### events

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

The current list of calendar events.

### handleSaveEvent

(`event`, `initiator?`) => `void` \| [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `undefined`

Callback when saving an event.

### handleDeleteEvent

(`eventId`, `initiator?`) => `void`

Callback when deleting an event.

### setSelectedEvent

(`event`) => `void`

State setter to select an event.

### setOpenEventDialog

(`open`) => `void`

State setter to open/close the event dialog.

## Returns

State and event handlers for the calendar.

### activeEvent

> **activeEvent**: [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

### handleEventDrag

> **handleEventDrag**: (`changes`, `interaction`) => `void`

#### Parameters

##### changes

`EventInteractionArgs`\<[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)\>

##### interaction?

[`GridInteraction`](../type-aliases/GridInteraction.md) = `"move"`

#### Returns

`void`

### handleSlotSelect

> **handleSlotSelect**: (`slotInfo`) => `void`

#### Parameters

##### slotInfo

`SlotInfo`

#### Returns

`void`

### handleSplitEvent

> **handleSplitEvent**: (`event`, `atMs`) => `void`

Cuts an event in two at a wall-clock instant (#657): the original keeps
its head and is trimmed to end at the cut, and a new event carrying the
same fields takes the tail. Durations are measured in *working* time, so
an event that jumps over a break keeps the same total after the cut.

#### Parameters

##### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

##### atMs

`number`

#### Returns

`void`

### setActiveEvent

> **setActiveEvent**: `Dispatch`\<`SetStateAction`\<[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`\>\>
