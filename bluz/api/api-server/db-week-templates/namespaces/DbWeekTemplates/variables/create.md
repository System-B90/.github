[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-week-templates](../../../index.md) / [DbWeekTemplates](../index.md) / create

# Variable: create

> `const` **create**: (`payload`, `author`, `seedEvents`, `controller`) => `Promise`\<[`WeekTemplate`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md)\> = `createTemplate`

Defined in: [ui/src/api-server/db-week-templates.ts:333](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/db-week-templates.ts#L333)

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
