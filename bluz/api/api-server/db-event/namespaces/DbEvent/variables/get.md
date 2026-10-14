[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / get

# Variable: get

> `const` **get**: (`eventId`, `options?`, `controller`) => `Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md) \| `null`\> = `getDbEvent`

Defined in: [ui/src/api-server/db-event.ts:584](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/db-event.ts#L584)

## Parameters

### eventId

`string`

### options?

`FindOptions`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md) \| `null`\>
