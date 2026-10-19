[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / getInRange

# Variable: getInRange

> `const` **getInRange**: (`startDate`, `endDate`, `options?`, `filter?`, `controller`) => `Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]\> = `getDbEventsInRange`

Defined in: [ui/src/api-server/db-event.ts:685](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/db-event.ts#L685)

## Parameters

### startDate

`Date`

### endDate

`Date`

### options?

`FindOptions`

### filter?

`Filter`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)\>

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]\>
