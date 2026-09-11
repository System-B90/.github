[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / planCurriculumCut

# Function: planCurriculumCut()

> **planCurriculumCut**(`curriculumId`, `options?`): `Promise`\<\{ `error`: [`ApiCurriculumCutError`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutError.md); `ok`: `false`; \} \| \{ `ok`: `true`; `result`: [`ApiCurriculumCutPlanResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPlanResponse.md); \}\>

Defined in: [ui/src/api-server/gantt/cut.ts:1018](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/cut.ts#L1018)

The "plan" half of the plan-then-confirm cut flow.

Runs the entire pipeline the commit would run — balance, constraint solve,
break pass — against the real iteration settings, and returns what it would
do plus every question it could not answer on its own. Writes nothing (no
courses are created either), so the dialog can walk the user through the
decisions one at a time and only then POST the commit with their answers.

Gating mirrors the commit so the dialog never asks questions about a cut that
would be refused anyway.

## Parameters

### curriculumId

`string`

### options?

[`CutPlanOptions`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanOptions.md) = `{}`

## Returns

`Promise`\<\{ `error`: [`ApiCurriculumCutError`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutError.md); `ok`: `false`; \} \| \{ `ok`: `true`; `result`: [`ApiCurriculumCutPlanResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPlanResponse.md); \}\>
