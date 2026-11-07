[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-week-templates](../../../index.md) / [DbWeekTemplates](../index.md) / getEvents

# Variable: getEvents

> `const` **getEvents**: (`id`, `courses`) => `Promise`\<[`WeekTemplateEventDocument`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplateEventDocument.md)[]\> = `getTemplateEvents`

Defined in: [ui/src/api-server/db-week-templates.ts:336](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/db-week-templates.ts#L336)

A template's events for one iteration: course names resolved to that
iteration's course ids, names it lacks dropped. Times stay in the
reference week; the caller places them into a real week.

## Parameters

### id

`string`

### courses

[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)[]

## Returns

`Promise`\<[`WeekTemplateEventDocument`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplateEventDocument.md)[]\>
