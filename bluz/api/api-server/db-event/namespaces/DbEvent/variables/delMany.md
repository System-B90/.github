[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / delMany

# Variable: delMany

> `const` **delMany**: (`eventIds`, `options?`, `controller`, `iterationId?`, `origin`) => `Promise`\<`void`\> = `deleteDbEvents`

Defined in: [ui/src/api-server/db-event.ts:693](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/db-event.ts#L693)

Bulk [deleteDbEvent](del.md): one updateMany, one history insert (#932).

## Parameters

### eventIds

`string`[]

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
