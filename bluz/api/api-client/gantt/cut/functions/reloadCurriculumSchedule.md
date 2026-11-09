[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/cut](../index.md) / reloadCurriculumSchedule

# Function: reloadCurriculumSchedule()

> **reloadCurriculumSchedule**(`curriculumId`, `options?`): `Promise`\<[`ApiCurriculumReloadResponse`](../../../../api-shared/types/gantt/reload/type-aliases/ApiCurriculumReloadResponse.md)\>

Defined in: [ui/src/api-client/gantt/cut.ts:129](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-client/gantt/cut.ts#L129)

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
