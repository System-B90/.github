[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/gantt](../index.md) / requireCurriculumId

# Function: requireCurriculumId()

> **requireCurriculumId**(`args`, `context`): `string`

Defined in: [ui/src/api-server/ai/tools/gantt.ts:25](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/tools/gantt.ts#L25)

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
