[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-mappings](../index.md) / updateCurriculumModuleDayMapping

# Function: updateCurriculumModuleDayMapping()

> **updateCurriculumModuleDayMapping**(`curriculumId`, `moduleId`, `eventId`, `oldMapping`, `newValues`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-mappings.ts:123](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/db-mappings.ts#L123)

Updates an existing mapping (e.g., moving a module to a different day/week).
Uses the composite primary key fields for identification.

## Parameters

### curriculumId

`string`

The curriculum identifier.

### moduleId

`string`

The module identifier.

### eventId

`string` \| `null`

The event identifier (or null if mapping a module only).

### oldMapping

The old day mapping coordinates.

#### dayId

`string`

### newValues

The new values to apply.

#### allottedMinutes?

`number`

#### dayId?

`string`

#### sortOrder?

`number`

#### weekOnly?

`boolean`

## Returns

`Promise`\<`object`[]\>

The updated mapping record.
