[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/week-templates](../index.md) / apiGetWeekTemplate

# Function: apiGetWeekTemplate()

> **apiGetWeekTemplate**(`id`, `weekStart`, `iterationId?`): `Promise`\<\{ `events`: [`Event`](../../../api-shared/types/event/type-aliases/Event.md)[]; `template`: [`WeekTemplate`](../../../api-shared/types/week-template/type-aliases/WeekTemplate.md); \}\>

Defined in: [ui/src/api-client/week-templates.ts:49](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-client/week-templates.ts#L49)

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
