[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasLecturers

# Function: eventHasLecturers()

> **eventHasLecturers**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:191](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-shared/types/event.ts#L191)

Checks if an event type carries a `lecturers` selection (lectures have
"מרצים"; workshops reuse the same field, labeled "מנהלים").

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

true if the lecturers field applies to this event type.
