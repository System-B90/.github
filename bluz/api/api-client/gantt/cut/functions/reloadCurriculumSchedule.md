[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/cut](../index.md) / reloadCurriculumSchedule

# Function: reloadCurriculumSchedule()

> **reloadCurriculumSchedule**(`curriculumId`, `options?`): `Promise`\<[`ApiCurriculumReloadResponse`](../../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadResponse.md)\>

Defined in: [ui/src/api-client/gantt/cut.ts:110](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-client/gantt/cut.ts#L110)

PATCH /api/gantt/curriculums/[id]/cut — reload an already-cut schedule from
the current gantt. With `dryRun` the server only computes the diff.

## Parameters

### curriculumId

`string`

Curriculum to reload from.

### options?

[`ApiCurriculumReloadPayload`](../../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadPayload.md) = `{}`

## Returns

`Promise`\<[`ApiCurriculumReloadResponse`](../../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadResponse.md)\>
