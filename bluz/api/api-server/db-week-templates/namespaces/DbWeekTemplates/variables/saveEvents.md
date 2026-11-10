[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-week-templates](../../../index.md) / [DbWeekTemplates](../index.md) / saveEvents

# Variable: saveEvents

> `const` **saveEvents**: (`id`, `events`, `author`, `controller`) => `Promise`\<[`WeekTemplate`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md)\> = `saveTemplateEvents`

Defined in: [ui/src/api-server/db-week-templates.ts:337](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/db-week-templates.ts#L337)

Replace a template's events. Each is moved into the reference week and
stamped with the names of its courses in `controller`'s iteration, which is
what later maps it onto any other iteration.

## Parameters

### id

`string`

### events

[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

### author

`string`

### controller

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md)

## Returns

`Promise`\<[`WeekTemplate`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md)\>
