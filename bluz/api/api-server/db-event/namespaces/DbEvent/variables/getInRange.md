[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-event](../../../index.md) / [DbEvent](../index.md) / getInRange

# Variable: getInRange

> `const` **getInRange**: (`startDate`, `endDate`, `options?`, `filter?`, `controller`) => `Promise`\<[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]\> = `getDbEventsInRange`

Defined in: [ui/src/api-server/db-event.ts:807](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/api-server/db-event.ts#L807)

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
