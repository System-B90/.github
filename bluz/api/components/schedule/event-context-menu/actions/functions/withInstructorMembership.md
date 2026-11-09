[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / withInstructorMembership

# Function: withInstructorMembership()

> **withInstructorMembership**(`event`, `instructorId`, `member`): [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:121](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/event-context-menu/actions.ts#L121)

Adds or removes one instructor (מבזר) from an event, leaving the rest of
its roster alone. A removed instructor leaves `lecturers` too, so a lecture
cannot keep naming them. Other lecturers stay: one dropped straight into
the lecturer list is not an instructor, and lost it on any toggle.

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
