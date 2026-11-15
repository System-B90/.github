[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasCourses

# Function: eventHasCourses()

> **eventHasCourses**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:260](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-shared/types/event.ts#L260)

Checks if an event type is assigned to specific courses. Prayers apply to
everyone, so they carry none; an unavailability belongs to a person, not a
course.

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

true if the courses field applies to this event type.
