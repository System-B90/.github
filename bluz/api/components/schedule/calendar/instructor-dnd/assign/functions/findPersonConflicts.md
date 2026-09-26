[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/assign](../index.md) / findPersonConflicts

# Function: findPersonConflicts()

> **findPersonConflicts**(`events`, `personId`, `target`, `excludeEventIds?`): [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/assign.ts:137](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/instructor-dnd/assign.ts#L137)

Finds events that already book a person during the target event's slot —
the same overlap report the curriculum cut pipeline surfaces.

## Parameters

### events

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

All events currently in state.

### personId

[`PersonId`](../../../../../../api-shared/types/event/type-aliases/PersonId.md)

The person being assigned.

### target

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

The event being dropped onto.

### excludeEventIds?

readonly `string`[] = `[]`

Events to leave out of the scan besides the target.
A move runs the target assign before the source unassign, so without this
the source event itself — still holding the person in state — reported as
a conflict on every move between overlapping events.

## Returns

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

Overlapping events the person is already busy in.
