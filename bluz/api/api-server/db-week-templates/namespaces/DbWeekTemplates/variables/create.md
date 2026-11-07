[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-week-templates](../../../index.md) / [DbWeekTemplates](../index.md) / create

# Variable: create

> `const` **create**: (`payload`, `author`, `seedEvents`, `controller`) => `Promise`\<[`WeekTemplate`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md)\> = `createTemplate`

Defined in: [ui/src/api-server/db-week-templates.ts:333](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/db-week-templates.ts#L333)

## Parameters

### payload

[`ApiWeekTemplateCreatePayload`](../../../../../api-shared/types/week-template/type-aliases/ApiWeekTemplateCreatePayload.md)

### author

`string`

### seedEvents

[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

### controller

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)

## Returns

`Promise`\<[`WeekTemplate`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md)\>
