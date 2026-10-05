[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasCourses

# Function: eventHasCourses()

> **eventHasCourses**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:231](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/event.ts#L231)

Checks if an event type is assigned to specific courses. Prayers apply to
everyone, so they carry none. Deliberately its own predicate rather than a
reuse of [eventHasRoom](eventHasRoom.md): the two only coincide today.

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

true if the courses field applies to this event type.
