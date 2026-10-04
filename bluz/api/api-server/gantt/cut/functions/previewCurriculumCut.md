[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / previewCurriculumCut

# Function: previewCurriculumCut()

> **previewCurriculumCut**(`curriculumId`, `options?`): `Promise`\<[`ApiCurriculumCutPreviewResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPreviewResponse.md)\>

Defined in: [ui/src/api-server/gantt/cut.ts:670](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/cut.ts#L670)

Dry-run of the cut (CLI preview route, AI preview tool): runs the exact same
pipeline as `cutCurriculumToSchedule` up to and including `planCut`, but
skips every gate (draft, iteration link, already-cut) and writes nothing.
Schedule timing settings come from the linked iteration when one exists,
falling back to the defaults otherwise so drafts still preview.

## Parameters

### curriculumId

`string`

### options?

[`CutPlanOptions`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanOptions.md) = `{}`

## Returns

`Promise`\<[`ApiCurriculumCutPreviewResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPreviewResponse.md)\>
