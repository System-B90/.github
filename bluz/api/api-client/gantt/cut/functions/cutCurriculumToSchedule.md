[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/cut](../index.md) / cutCurriculumToSchedule

# Function: cutCurriculumToSchedule()

> **cutCurriculumToSchedule**(`curriculumId`, `options?`): `Promise`\<[`ApiCurriculumCutResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutResponse.md)\>

Defined in: [ui/src/api-client/gantt/cut.ts:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/cut.ts#L28)

POST /api/gantt/curriculums/[id]/cut — materialize a published, linked
curriculum into schedule events. Resolves to the cut summary, or throws a
[CurriculumCutError](../../../../api-shared/types/gantt/cut/classes/CurriculumCutError.md) carrying the coded reason on a 4xx.

## Parameters

### curriculumId

`string`

### options?

[`ApiCurriculumCutPayload`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPayload.md) = `{}`

## Returns

`Promise`\<[`ApiCurriculumCutResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutResponse.md)\>
