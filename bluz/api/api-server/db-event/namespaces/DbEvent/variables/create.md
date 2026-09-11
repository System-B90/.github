[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / create

# Variable: create

> `const` **create**: (`eventData`, `options?`, `controller`, `iterationId?`, `origin`) => `Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)\> = `createDbEvent`

Defined in: [ui/src/api-server/db-event.ts:316](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-event.ts#L316)

Inserts a new calendar event into the MongoDB collection.
Triggers a real-time WebSocket broadcast to notify clients of the new event.

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

The fixed, created DbEventDocument.

## Throws

ClientApiError if the event ID is missing.

## Example

```typescript
const newEvent = await DbEvent.create(eventPayload);
```
