[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/execution](../index.md) / recreateExecutionOccurrence

# Function: recreateExecutionOccurrence()

> **recreateExecutionOccurrence**(`curriculumId`, `ganttEventId`, `occurrenceDate`): `Promise`\<\{ `createdEvents`: `number`; \}\>

Defined in: [ui/src/api-client/gantt/execution.ts:22](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-client/gantt/execution.ts#L22)

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
