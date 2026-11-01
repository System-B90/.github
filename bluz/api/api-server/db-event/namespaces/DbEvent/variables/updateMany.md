[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / updateMany

# Variable: updateMany

> `const` **updateMany**: (`events`, `options?`, `controller`, `iterationId?`, `origin`) => `Promise`\<\{ `after`: [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]; `before`: `Map`\<`string`, [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)\>; \}\> = `updateDbEvents`

Defined in: [ui/src/api-server/db-event.ts:798](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/db-event.ts#L798)

[setDbEvents](setMany.md) that also returns the stored copies, keyed by id (#926).

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

`Promise`\<\{ `after`: [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]; `before`: `Map`\<`string`, [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)\>; \}\>
