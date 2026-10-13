[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / getInRange

# Variable: getInRange

> `const` **getInRange**: (`startDate`, `endDate`, `options?`, `filter?`, `controller`) => `Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]\> = `getDbEventsInRange`

Defined in: [ui/src/api-server/db-event.ts:586](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/db-event.ts#L586)

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
