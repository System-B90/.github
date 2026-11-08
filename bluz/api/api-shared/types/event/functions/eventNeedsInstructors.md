[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventNeedsInstructors

# Function: eventNeedsInstructors()

> **eventNeedsInstructors**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:201](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types/event.ts#L201)

Whether an event type is expected to have a מבזר, i.e. whether one missing
is worth flagging. Prayers and breaks run without one — a break may still
carry instructors, it just never warns when it has none.

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

false for prayers and breaks.
