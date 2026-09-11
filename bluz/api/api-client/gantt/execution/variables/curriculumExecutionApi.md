[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/execution](../index.md) / curriculumExecutionApi

# Variable: curriculumExecutionApi

> `const` **curriculumExecutionApi**: `object`

Defined in: [ui/src/api-client/gantt/execution.ts:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/execution.ts#L18)

## Type Declaration

### get

> `readonly` **get**: (`curriculumId`) => `Promise`\<[`ApiCurriculumExecutionResponse`](../../../../api-shared/types/gantt/execution/type-aliases/ApiCurriculumExecutionResponse.md)\> = `fetchCurriculumExecution`

GET /api/gantt/curriculums/[id]/execution — תכנון מול ביצוע comparison for a
curriculum. Resolves to `{ events: {} }` when the curriculum has not been
cut into a schedule yet.

#### Parameters

##### curriculumId

`string`

#### Returns

`Promise`\<[`ApiCurriculumExecutionResponse`](../../../../api-shared/types/gantt/execution/type-aliases/ApiCurriculumExecutionResponse.md)\>
