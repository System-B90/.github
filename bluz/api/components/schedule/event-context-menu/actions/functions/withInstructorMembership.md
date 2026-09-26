[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / withInstructorMembership

# Function: withInstructorMembership()

> **withInstructorMembership**(`event`, `instructorId`, `member`): [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:115](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/actions.ts#L115)

Adds or removes one instructor (מבזר) from an event, leaving the rest of
its roster alone. `lecturers` is filtered down to whoever is still on the
event, so a lecture cannot keep naming a lecturer who is no longer
assigned to it.

## Parameters

### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The event to change.

### instructorId

`number`

The instructor being toggled.

### member

`boolean`

Whether the event should end up staffed by them.

## Returns

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The updated event.
