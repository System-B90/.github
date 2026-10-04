[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/execution](../index.md) / recreateExecutionOccurrence

# Function: recreateExecutionOccurrence()

> **recreateExecutionOccurrence**(`curriculumId`, `ganttEventId`, `occurrenceDate`): `Promise`\<\{ `createdEvents`: `number`; \}\>

Defined in: [ui/src/api-client/gantt/execution.ts:22](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-client/gantt/execution.ts#L22)

POST /api/gantt/curriculums/[id]/execution/recreate — re-create the schedule
event for one deleted cut occurrence (#682).

## Parameters

### curriculumId

`string`

### ganttEventId

`string`

### occurrenceDate

`string`

## Returns

`Promise`\<\{ `createdEvents`: `number`; \}\>
