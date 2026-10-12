[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / setMany

# Variable: setMany

> `const` **setMany**: (`events`, `options?`, `controller`, `iterationId?`, `origin`) => `Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]\> = `setDbEvents`

Defined in: [ui/src/api-server/db-event.ts:591](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-server/db-event.ts#L591)

Bulk [setDbEvent](set.md): one read, one bulkWrite, one history insertMany and
one broadcast for the whole batch instead of N of each (#932).

## Parameters

### events

[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

### options?

`FindOptions`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

### origin?

[`EventWriteOrigin`](../../../../db-event-history/type-aliases/EventWriteOrigin.md) = `UNKNOWN_ORIGIN`

## Returns

`Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]\>

## Throws

ClientApiError if any id is missing or not found; nothing is
broadcast or logged in that case.
