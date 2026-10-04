[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/cut](../index.md) / curriculumCutApi

# Variable: curriculumCutApi

> `const` **curriculumCutApi**: `object`

Defined in: [ui/src/api-client/gantt/cut.ts:130](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-client/gantt/cut.ts#L130)

## Type Declaration

### cut

> `readonly` **cut**: (`curriculumId`, `options`) => `Promise`\<[`ApiCurriculumCutResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutResponse.md)\> = `cutCurriculumToSchedule`

POST /api/gantt/curriculums/[id]/cut — materialize a published, linked
curriculum into schedule events. Resolves to the cut summary, or throws a
[CurriculumCutError](../../../../api-shared/types/gantt/cut/classes/CurriculumCutError.md) carrying the coded reason on a 4xx.

#### Parameters

##### curriculumId

`string`

##### options?

[`ApiCurriculumCutPayload`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPayload.md) = `{}`

#### Returns

`Promise`\<[`ApiCurriculumCutResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutResponse.md)\>

### plan

> `readonly` **plan**: (`curriculumId`, `options`) => `Promise`\<[`ApiCurriculumCutPlanResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPlanResponse.md)\> = `planCurriculumCut`

POST /api/gantt/curriculums/[id]/cut/plan — the "plan" half of the
plan-then-confirm flow. Runs the full cut pipeline without writing and
returns what it would do plus the open decisions the dialog must ask about.

#### Parameters

##### curriculumId

`string`

##### options?

[`ApiCurriculumCutPayload`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPayload.md) = `{}`

#### Returns

`Promise`\<[`ApiCurriculumCutPlanResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutPlanResponse.md)\>

### pullBack

> `readonly` **pullBack**: (`curriculumId`) => `Promise`\<[`ApiCurriculumPullBackResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumPullBackResponse.md)\> = `pullBackCurriculumSchedule`

DELETE /api/gantt/curriculums/[id]/cut — soft-delete every schedule event a
previous cut generated. Throws a [CurriculumPullBackError](../../../../api-shared/types/gantt/cut/classes/CurriculumPullBackError.md) carrying the
coded reason on a 4xx.

#### Parameters

##### curriculumId

`string`

#### Returns

`Promise`\<[`ApiCurriculumPullBackResponse`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumPullBackResponse.md)\>

### reload

> `readonly` **reload**: (`curriculumId`, `options`) => `Promise`\<[`ApiCurriculumReloadResponse`](../../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadResponse.md)\> = `reloadCurriculumSchedule`

PATCH /api/gantt/curriculums/[id]/cut — reload an already-cut schedule from
the current gantt. With `dryRun` the server only computes the diff.

#### Parameters

##### curriculumId

`string`

Curriculum to reload from.

##### options?

[`ApiCurriculumReloadPayload`](../../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadPayload.md) = `{}`

#### Returns

`Promise`\<[`ApiCurriculumReloadResponse`](../../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadResponse.md)\>

### status

> `readonly` **status**: (`curriculumId`) => `Promise`\<[`ApiCurriculumCutStatus`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutStatus.md)\> = `getCurriculumCutStatus`

GET /api/gantt/curriculums/[id]/cut — whether the curriculum currently holds
live cut events, used to toggle between the "cut" and "pull back" actions.

#### Parameters

##### curriculumId

`string`

#### Returns

`Promise`\<[`ApiCurriculumCutStatus`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutStatus.md)\>
