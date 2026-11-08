[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/assign](../index.md) / withPersonRemoved

# Function: withPersonRemoved()

> **withPersonRemoved**(`event`, `personId`): [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/assign.ts:108](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/calendar/instructor-dnd/assign.ts#L108)

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
