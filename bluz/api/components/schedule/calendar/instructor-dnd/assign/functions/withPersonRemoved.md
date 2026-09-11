[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/assign](../index.md) / withPersonRemoved

# Function: withPersonRemoved()

> **withPersonRemoved**(`event`, `personId`): [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/assign.ts:106](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/instructor-dnd/assign.ts#L106)

Removes a person from both person fields of an event.

## Parameters

### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

The event to update.

### personId

[`PersonId`](../../../../../../api-shared/types/event/type-aliases/PersonId.md)

The person being unassigned.

## Returns

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

An updated event copy, or `null` when the person was not on the
event to begin with.
