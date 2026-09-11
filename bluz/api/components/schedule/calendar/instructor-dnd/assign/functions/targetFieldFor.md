[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/assign](../index.md) / targetFieldFor

# Function: targetFieldFor()

> **targetFieldFor**(`event`, `withModifier`, `sourceField?`): [`PersonField`](../../types/type-aliases/PersonField.md)

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/assign.ts:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/instructor-dnd/assign.ts#L24)

Resolves which person field a drop writes into.

## Parameters

### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

The drop target event.

### withModifier

`boolean`

Whether Shift was held at drop time.

### sourceField?

[`PersonField`](../../types/type-aliases/PersonField.md)

The field the person was dragged out of, when the drag
started on a chip already sitting in an event. A move keeps the person's
role: dragging a lecturer without Shift used to silently demote them to an
instructor on the target (#628).

## Returns

[`PersonField`](../../types/type-aliases/PersonField.md)

`lecturers` when the modifier is held or the person already was a
lecturer, and the event type actually carries lecturers; `instructors`
otherwise.
