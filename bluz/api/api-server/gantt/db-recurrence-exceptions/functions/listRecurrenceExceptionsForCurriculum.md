[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-recurrence-exceptions](../index.md) / listRecurrenceExceptionsForCurriculum

# Function: listRecurrenceExceptionsForCurriculum()

> **listRecurrenceExceptionsForCurriculum**(`curriculumId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-recurrence-exceptions.ts:20](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/gantt/db-recurrence-exceptions.ts#L20)

Retrieves every recurrence exception (deleted/materialized occurrence day)
for a curriculum, keyed for cheap client-side lookup.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<`object`[]\>
