[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/execution](../index.md) / getCurriculumExecution

# Function: getCurriculumExecution()

> **getCurriculumExecution**(`curriculumId`): `Promise`\<[`ApiCurriculumExecutionResponse`](../../../../api-shared/types/gantt/execution/type-aliases/ApiCurriculumExecutionResponse.md)\>

Defined in: [ui/src/api-server/gantt/execution.ts:48](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-server/gantt/execution.ts#L48)

Compute the plan-vs-execution comparison for a curriculum. Returns
`{ events: {} }` when there is no linked iteration or the curriculum was
never cut.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<[`ApiCurriculumExecutionResponse`](../../../../api-shared/types/gantt/execution/type-aliases/ApiCurriculumExecutionResponse.md)\>
