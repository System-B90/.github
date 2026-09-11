[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/cut](../index.md) / previewCurriculumCut

# Function: previewCurriculumCut()

> **previewCurriculumCut**(`curriculumId`): `Promise`\<[`ApiCurriculumCutPreviewResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPreviewResponse.md)\>

Defined in: [ui/src/api-client/gantt/cut.ts:107](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/cut.ts#L107)

GET /api/gantt/curriculums/[id]/cut/preview — dry-run of the cut planner:
dated, timed occurrences (or the planner's validation errors), no writes.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<[`ApiCurriculumCutPreviewResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPreviewResponse.md)\>
