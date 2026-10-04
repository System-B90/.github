[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/cut](../index.md) / planCurriculumCut

# Function: planCurriculumCut()

> **planCurriculumCut**(`curriculumId`, `options?`): `Promise`\<[`ApiCurriculumCutPlanResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPlanResponse.md)\>

Defined in: [ui/src/api-client/gantt/cut.ts:49](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-client/gantt/cut.ts#L49)

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
