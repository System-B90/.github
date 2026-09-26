[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / set

# Variable: set

> `const` **set**: (`eventData`, `options?`, `controller`, `iterationId?`, `origin`) => `Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)\> = `setDbEvent`

Defined in: [ui/src/api-server/db-event.ts:314](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/db-event.ts#L314)

Updates an existing calendar event in the MongoDB collection.
Triggers a real-time WebSocket broadcast to all connected clients.

## Parameters

### eventData

[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

The document payload sent by the client. Must contain a valid `id` UUID.

### options?

`FindOptions`

MongoDB FindOptions.

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

### origin?

[`EventWriteOrigin`](../../../../db-event-history/type-aliases/EventWriteOrigin.md) = `UNKNOWN_ORIGIN`

## Returns

`Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)\>

The fixed and serialized DbEventDocument.

## Throws

ClientApiError if the event ID is missing or the event is not found in the database.

## Example

```typescript
const updated = await DbEvent.set(eventPayload);
```
