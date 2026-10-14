[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-recurrence-exceptions](../index.md) / listRecurrenceExceptionsForCurriculum

# Function: listRecurrenceExceptionsForCurriculum()

> **listRecurrenceExceptionsForCurriculum**(`curriculumId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-recurrence-exceptions.ts:19](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/gantt/db-recurrence-exceptions.ts#L19)

Retrieves every recurrence exception (deleted/materialized occurrence day)
for a curriculum, keyed for cheap client-side lookup.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<`object`[]\>
