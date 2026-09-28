[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/gantt](../index.md) / requireCurriculumId

# Function: requireCurriculumId()

> **requireCurriculumId**(`args`, `context`): `string`

Defined in: [ui/src/api-server/ai/tools/gantt.ts:24](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-server/ai/tools/gantt.ts#L24)

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
