[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / reassignedToRoom

# Function: reassignedToRoom()

> **reassignedToRoom**(`event`, `room`): [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:94](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/actions.ts#L94)

Reassigns the event to exactly one room, or clears its rooms entirely.
"Reassign" replaces rather than adds: an event dragged between room columns
behaves the same way, and a menu that only ever appended would give no way
back out of a wrong room without opening the dialog.

## Parameters

### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The event to change.

### room

[`ResolvableRoom`](../../../../../api-shared/types/room/type-aliases/ResolvableRoom.md) \| `null`

The room to move it to, or null to leave it roomless.

## Returns

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The updated event.
