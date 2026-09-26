[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasCourses

# Function: eventHasCourses()

> **eventHasCourses**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:231](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/event.ts#L231)

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
