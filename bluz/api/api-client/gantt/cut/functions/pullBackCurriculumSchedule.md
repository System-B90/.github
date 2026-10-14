[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/cut](../index.md) / pullBackCurriculumSchedule

# Function: pullBackCurriculumSchedule()

> **pullBackCurriculumSchedule**(`curriculumId`): `Promise`\<[`ApiCurriculumPullBackResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumPullBackResponse.md)\>

Defined in: [ui/src/api-client/gantt/cut.ts:83](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-client/gantt/cut.ts#L83)

DELETE /api/gantt/curriculums/[id]/cut — soft-delete every schedule event a
previous cut generated. Throws a [CurriculumPullBackError](../../../../api-shared/types/gantt/cut/classes/CurriculumPullBackError.md) carrying the
coded reason on a 4xx.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<[`ApiCurriculumPullBackResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumPullBackResponse.md)\>
