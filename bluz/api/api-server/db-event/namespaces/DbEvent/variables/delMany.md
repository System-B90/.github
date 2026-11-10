[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / delMany

# Variable: delMany

> `const` **delMany**: (`eventIds`, `options?`, `controller`, `iterationId?`, `origin`) => `Promise`\<`void`\> = `deleteDbEvents`

Defined in: [ui/src/api-server/db-event.ts:815](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/db-event.ts#L815)

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
