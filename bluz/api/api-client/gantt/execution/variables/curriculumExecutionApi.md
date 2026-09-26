[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/execution](../index.md) / curriculumExecutionApi

# Variable: curriculumExecutionApi

> `const` **curriculumExecutionApi**: `object`

Defined in: [ui/src/api-client/gantt/execution.ts:36](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/gantt/execution.ts#L36)

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

### recreateOccurrence

> `readonly` **recreateOccurrence**: (`curriculumId`, `ganttEventId`, `occurrenceDate`) => `Promise`\<\{ `createdEvents`: `number`; \}\> = `recreateExecutionOccurrence`

POST /api/gantt/curriculums/[id]/execution/recreate — re-create the schedule
event for one deleted cut occurrence (#682).

#### Parameters

##### curriculumId

`string`

##### ganttEventId

`string`

##### occurrenceDate

`string`

#### Returns

`Promise`\<\{ `createdEvents`: `number`; \}\>
