[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / update

# Variable: update

> `const` **update**: (`eventData`, `options?`, `controller`, `iterationId?`, `origin`) => `Promise`\<\{ `after`: [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md); `before`: [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md); \}\> = `updateDbEvent`

Defined in: [ui/src/api-server/db-event.ts:588](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/db-event.ts#L588)

[setDbEvent](set.md) that also returns the stored copy it replaced, so callers
that need the old version (the Google fan-out) don't read it again (#926).
Read and write are one atomic `findOneAndUpdate`, so `before` is exactly
what was overwritten.

## Parameters

### eventData

[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

### options?

`FindOptions`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

### origin?

[`EventWriteOrigin`](../../../../db-event-history/type-aliases/EventWriteOrigin.md) = `UNKNOWN_ORIGIN`

## Returns

`Promise`\<\{ `after`: [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md); `before`: [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md); \}\>
