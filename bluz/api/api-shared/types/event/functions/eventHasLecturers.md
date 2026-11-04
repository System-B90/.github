[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasLecturers

# Function: eventHasLecturers()

> **eventHasLecturers**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:183](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/event.ts#L183)

Checks if an event type carries a `lecturers` selection (lectures have
"מרצים"; workshops reuse the same field, labeled "מנהלים").

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

true if the lecturers field applies to this event type.
