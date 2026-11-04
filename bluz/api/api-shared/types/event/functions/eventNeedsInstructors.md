[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventNeedsInstructors

# Function: eventNeedsInstructors()

> **eventNeedsInstructors**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:195](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/event.ts#L195)

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
