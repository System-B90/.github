[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/gantt](../index.md) / requireCurriculumId

# Function: requireCurriculumId()

> **requireCurriculumId**(`args`, `context`): `string`

Defined in: [ui/src/api-server/ai/tools/gantt.ts:24](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/gantt.ts#L24)

Resolves which curriculum a call targets: an explicit argument wins, and the
screen the user is on is the fallback, so "תגזור את זה" works without the
model having to guess an id.

## Parameters

### args

#### curriculumId?

`string`

### context

[`AiToolContext`](../../types/type-aliases/AiToolContext.md)

## Returns

`string`
