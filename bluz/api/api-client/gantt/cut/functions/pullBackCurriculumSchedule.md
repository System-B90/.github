[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/cut](../index.md) / pullBackCurriculumSchedule

# Function: pullBackCurriculumSchedule()

> **pullBackCurriculumSchedule**(`curriculumId`): `Promise`\<[`ApiCurriculumPullBackResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumPullBackResponse.md)\>

Defined in: [ui/src/api-client/gantt/cut.ts:84](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/cut.ts#L84)

DELETE /api/gantt/curriculums/[id]/cut — soft-delete every schedule event a
previous cut generated. Throws a [CurriculumPullBackError](../../../../api-shared/types/gantt/cut/classes/CurriculumPullBackError.md) carrying the
coded reason on a 4xx.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<[`ApiCurriculumPullBackResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumPullBackResponse.md)\>
