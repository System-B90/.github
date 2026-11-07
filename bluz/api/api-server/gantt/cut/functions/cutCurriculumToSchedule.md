[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / cutCurriculumToSchedule

# Function: cutCurriculumToSchedule()

> **cutCurriculumToSchedule**(`curriculumId`, `options?`, `origin?`): `Promise`\<[`CutOutcome`](../type-aliases/CutOutcome.md)\>

Defined in: [ui/src/api-server/gantt/cut.ts:1769](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/gantt/cut.ts#L1769)

Materialize a published, linked curriculum into schedule events. Any gating
violation returns a structured error and writes nothing.

## Parameters

### curriculumId

`string`

### options?

[`CutWeekOptions`](../type-aliases/CutWeekOptions.md) = `{}`

### origin?

[`EventWriteOrigin`](../../../db-event-history/type-aliases/EventWriteOrigin.md) = `...`

## Returns

`Promise`\<[`CutOutcome`](../type-aliases/CutOutcome.md)\>
