[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / update

# Variable: update

> `const` **update**: (`eventData`, `options?`, `controller`, `iterationId?`, `origin`) => `Promise`\<\{ `after`: [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md); `before`: [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md); `stale?`: `boolean`; \}\> = `updateDbEvent`

Defined in: [ui/src/api-server/db-event.ts:687](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/db-event.ts#L687)

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

`Promise`\<\{ `after`: [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md); `before`: [`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md); `stale?`: `boolean`; \}\>
