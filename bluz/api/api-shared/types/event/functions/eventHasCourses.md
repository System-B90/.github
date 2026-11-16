[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasCourses

# Function: eventHasCourses()

> **eventHasCourses**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:260](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-shared/types/event.ts#L260)

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
