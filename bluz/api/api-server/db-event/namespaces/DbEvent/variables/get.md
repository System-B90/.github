[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / get

# Variable: get

> `const` **get**: (`eventId`, `options?`, `controller`) => `Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md) \| `null`\> = `getDbEvent`

Defined in: [ui/src/api-server/db-event.ts:311](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/db-event.ts#L311)

## Parameters

### eventId

`string`

### options?

`FindOptions`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md) \| `null`\>
