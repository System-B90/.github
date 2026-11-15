[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventNeedsRoom

# Function: eventNeedsRoom()

> **eventNeedsRoom**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:244](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-shared/types/event.ts#L244)

Whether a missing room is worth flagging. Prayers and breaks may sit in a
room but need not; an unavailability's room is the fixed pseudo-room.

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

false for prayers, breaks and unavailabilities.
