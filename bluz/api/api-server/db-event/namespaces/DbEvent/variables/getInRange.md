[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / getInRange

# Variable: getInRange

> `const` **getInRange**: (`startDate`, `endDate`, `options?`, `filter?`, `controller`) => `Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]\> = `getDbEventsInRange`

Defined in: [ui/src/api-server/db-event.ts:807](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/db-event.ts#L807)

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
