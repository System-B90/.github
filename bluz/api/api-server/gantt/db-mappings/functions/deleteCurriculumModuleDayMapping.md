[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-mappings](../index.md) / deleteCurriculumModuleDayMapping

# Function: deleteCurriculumModuleDayMapping()

> **deleteCurriculumModuleDayMapping**(`curriculumId`, `moduleId`, `eventId`, `dayId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-mappings.ts:218](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/gantt/db-mappings.ts#L218)

Deletes an existing curriculum day mapping.

## Parameters

### curriculumId

`string`

The curriculum identifier.

### moduleId

`string`

The module identifier.

### eventId

`string` \| `null`

The event identifier (or null if deleting a module mapping).

### dayId

`string`

The day identifier.

## Returns

`Promise`\<`object`[]\>

The deleted mapping record.
