[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/cut](../index.md) / getCurriculumCutStatus

# Function: getCurriculumCutStatus()

> **getCurriculumCutStatus**(`curriculumId`): `Promise`\<[`ApiCurriculumCutStatus`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutStatus.md)\>

Defined in: [ui/src/api-client/gantt/cut.ts:71](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/cut.ts#L71)

GET /api/gantt/curriculums/[id]/cut — whether the curriculum currently holds
live cut events, used to toggle between the "cut" and "pull back" actions.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<[`ApiCurriculumCutStatus`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutStatus.md)\>
