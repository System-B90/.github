[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / delMany

# Variable: delMany

> `const` **delMany**: (`eventIds`, `options?`, `controller`, `iterationId?`, `origin`) => `Promise`\<`void`\> = `deleteDbEvents`

Defined in: [ui/src/api-server/db-event.ts:800](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/db-event.ts#L800)

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
