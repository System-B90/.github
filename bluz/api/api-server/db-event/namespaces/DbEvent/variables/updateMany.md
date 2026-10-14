[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / updateMany

# Variable: updateMany

> `const` **updateMany**: (`events`, `options?`, `controller`, `iterationId?`, `origin`) => `Promise`\<\{ `after`: [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]; `before`: `Map`\<`string`, [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)\>; \}\> = `updateDbEvents`

Defined in: [ui/src/api-server/db-event.ts:592](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-server/db-event.ts#L592)

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
