[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-recurrence-exceptions](../index.md) / listRecurrenceExceptionsForCurriculum

# Function: listRecurrenceExceptionsForCurriculum()

> **listRecurrenceExceptionsForCurriculum**(`curriculumId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-recurrence-exceptions.ts:20](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/db-recurrence-exceptions.ts#L20)

Retrieves every recurrence exception (deleted/materialized occurrence day)
for a curriculum, keyed for cheap client-side lookup.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<`object`[]\>
