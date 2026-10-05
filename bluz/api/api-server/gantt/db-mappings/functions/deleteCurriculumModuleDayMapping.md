[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-mappings](../index.md) / deleteCurriculumModuleDayMapping

# Function: deleteCurriculumModuleDayMapping()

> **deleteCurriculumModuleDayMapping**(`curriculumId`, `moduleId`, `eventId`, `dayId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-mappings.ts:199](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/gantt/db-mappings.ts#L199)

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
