[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventNeedsRoom

# Function: eventNeedsRoom()

> **eventNeedsRoom**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:243](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types/event.ts#L243)

Whether a missing room is worth flagging. Prayers and breaks may sit in a
room but need not; an unavailability's room is the fixed pseudo-room.

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

false for prayers, breaks and unavailabilities.
