[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / del

# Variable: del

> `const` **del**: (`eventId`, `options?`, `controller`, `iterationId?`, `origin`) => `Promise`\<`void`\> = `deleteDbEvent`

Defined in: [ui/src/api-server/db-event.ts:315](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-event.ts#L315)

Soft-deletes a calendar event by setting its `archived` flag rather than
removing the document. Archived events are filtered out of every read path,
so to clients this is indistinguishable from a hard delete — but the record
is preserved for auditing/restore. The real-time broadcast still uses the
"removed" action so connected clients drop it from their views.

## Parameters

### eventId

`string`

### options?

`FindOptions`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

### origin?

[`EventWriteOrigin`](../../../../db-event-history/type-aliases/EventWriteOrigin.md) = `UNKNOWN_ORIGIN`

## Returns

`Promise`\<`void`\>
