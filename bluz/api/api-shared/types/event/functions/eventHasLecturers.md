[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasLecturers

# Function: eventHasLecturers()

> **eventHasLecturers**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:191](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/event.ts#L191)

Checks if an event type carries a `lecturers` selection (lectures have
"מרצים"; workshops reuse the same field, labeled "מנהלים").

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

true if the lecturers field applies to this event type.
