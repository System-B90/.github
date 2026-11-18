[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasRoom

# Function: eventHasRoom()

> **eventHasRoom**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:232](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/types/event.ts#L232)

Checks if an event type can be placed in a room (the room picker applies).
Prayers may carry one — "בית כנסת", say — but need not; see
[eventNeedsRoom](eventNeedsRoom.md).

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

true if the event type takes a room, false otherwise.

## Example

```typescript
if (eventHasRoom(event.type)) {
  // Render room picker field
}
```
