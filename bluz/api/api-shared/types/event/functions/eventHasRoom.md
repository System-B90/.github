[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventHasRoom

# Function: eventHasRoom()

> **eventHasRoom**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:214](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L214)

Checks if an event type is associated with a physical classroom/room.

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

true if the event type requires a room, false otherwise.

## Example

```typescript
if (eventHasRoom(event.type)) {
  // Render room picker field
}
```
