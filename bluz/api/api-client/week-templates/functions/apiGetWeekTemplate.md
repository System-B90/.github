[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/week-templates](../index.md) / apiGetWeekTemplate

# Function: apiGetWeekTemplate()

> **apiGetWeekTemplate**(`id`, `weekStart`, `iterationId?`): `Promise`\<\{ `events`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; `template`: [`WeekTemplate`](../../../api-shared/types/week-template/type-aliases/WeekTemplate.md); \}\>

Defined in: [ui/src/api-client/week-templates.ts:42](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-client/week-templates.ts#L42)

Fetches a template's events placed into the week starting `weekStart`
(Sunday, YYYY-MM-DD), with course ids of `iterationId`'s run.

## Parameters

### id

`string`

### weekStart

`string`

### iterationId?

`string`

## Returns

`Promise`\<\{ `events`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; `template`: [`WeekTemplate`](../../../api-shared/types/week-template/type-aliases/WeekTemplate.md); \}\>
