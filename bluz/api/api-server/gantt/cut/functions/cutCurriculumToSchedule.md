[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / cutCurriculumToSchedule

# Function: cutCurriculumToSchedule()

> **cutCurriculumToSchedule**(`curriculumId`, `options?`, `origin?`): `Promise`\<[`CutOutcome`](../type-aliases/CutOutcome.md)\>

Defined in: [ui/src/api-server/gantt/cut.ts:1162](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/gantt/cut.ts#L1162)

Materialize a published, linked curriculum into schedule events. Any gating
violation returns a structured error and writes nothing.

## Parameters

### curriculumId

`string`

### options?

[`CutPlanOptions`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanOptions.md) = `{}`

### origin?

[`EventWriteOrigin`](../../../db-event-history/type-aliases/EventWriteOrigin.md) = `...`

## Returns

`Promise`\<[`CutOutcome`](../type-aliases/CutOutcome.md)\>
