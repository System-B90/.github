[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/execution](../index.md) / fetchCurriculumExecution

# Function: fetchCurriculumExecution()

> **fetchCurriculumExecution**(`curriculumId`): `Promise`\<[`ApiCurriculumExecutionResponse`](../../../../api-shared/types/gantt/execution/type-aliases/ApiCurriculumExecutionResponse.md)\>

Defined in: [ui/src/api-client/gantt/execution.ts:10](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-client/gantt/execution.ts#L10)

GET /api/gantt/curriculums/[id]/execution — תכנון מול ביצוע comparison for a
curriculum. Resolves to `{ events: {} }` when the curriculum has not been
cut into a schedule yet.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<[`ApiCurriculumExecutionResponse`](../../../../api-shared/types/gantt/execution/type-aliases/ApiCurriculumExecutionResponse.md)\>
