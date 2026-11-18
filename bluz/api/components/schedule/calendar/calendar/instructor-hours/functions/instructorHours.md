[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/instructor-hours](../index.md) / instructorHours

# Function: instructorHours()

> **instructorHours**(`events`, `from`, `to`, `earlyBefore`): [`InstructorHours`](../type-aliases/InstructorHours.md)[]

Defined in: [ui/src/components/schedule/calendar/calendar/instructor-hours.ts:23](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/schedule/calendar/calendar/instructor-hours.ts#L23)

Minutes each staff member (instructors + staff lecturers) teaches inside
`[from, to)`, longest first, plus how many days they start early. Overlapping
events of one person count once — a double booking is still one hour of
their time. Parked events, unavailabilities, breaks and prayers are not
teaching.

## Parameters

### events

readonly [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

### from

`number`

### to

`number`

### earlyBefore

`number`

Minutes after midnight; teaching that starts before it
       makes the day an early one.

## Returns

[`InstructorHours`](../type-aliases/InstructorHours.md)[]
