[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/assign](../index.md) / withPersonAdded

# Function: withPersonAdded()

> **withPersonAdded**(`event`, `personId`, `field`): [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/assign.ts:84](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/instructor-dnd/assign.ts#L84)

Adds a person to one of an event's person fields.

## Parameters

### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

The event to update.

### personId

[`PersonId`](../../../../../../api-shared/types/event/type-aliases/PersonId.md)

The person being assigned.

### field

[`PersonField`](../../types/type-aliases/PersonField.md)

The field to write into.

## Returns

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `null`

An updated event copy, or `null` when the person already holds that
exact role on the event (nothing to save).
