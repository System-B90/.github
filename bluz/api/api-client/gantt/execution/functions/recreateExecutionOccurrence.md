[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/execution](../index.md) / recreateExecutionOccurrence

# Function: recreateExecutionOccurrence()

> **recreateExecutionOccurrence**(`curriculumId`, `ganttEventId`, `occurrenceDate`): `Promise`\<\{ `createdEvents`: `number`; \}\>

Defined in: [ui/src/api-client/gantt/execution.ts:23](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-client/gantt/execution.ts#L23)

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
