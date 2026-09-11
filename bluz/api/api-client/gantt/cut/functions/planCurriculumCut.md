[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/cut](../index.md) / planCurriculumCut

# Function: planCurriculumCut()

> **planCurriculumCut**(`curriculumId`, `options?`): `Promise`\<[`ApiCurriculumCutPlanResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPlanResponse.md)\>

Defined in: [ui/src/api-client/gantt/cut.ts:50](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/cut.ts#L50)

POST /api/gantt/curriculums/[id]/cut/plan — the "plan" half of the
plan-then-confirm flow. Runs the full cut pipeline without writing and
returns what it would do plus the open decisions the dialog must ask about.

## Parameters

### curriculumId

`string`

### options?

[`ApiCurriculumCutPayload`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPayload.md) = `{}`

## Returns

`Promise`\<[`ApiCurriculumCutPlanResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPlanResponse.md)\>
