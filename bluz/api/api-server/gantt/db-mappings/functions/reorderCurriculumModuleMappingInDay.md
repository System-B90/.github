[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-mappings](../index.md) / reorderCurriculumModuleMappingInDay

# Function: reorderCurriculumModuleMappingInDay()

> **reorderCurriculumModuleMappingInDay**(`curriculumId`, `moduleId`, `eventId`, `dayId`, `newSortOrder`): `Promise`\<`RowList`\<`never`[]\>\>

Defined in: [ui/src/api-server/gantt/db-mappings.ts:165](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/gantt/db-mappings.ts#L165)

Reorders modules or events within a specific day.
Implements a fractional/float-based update for the sortOrder.

## Parameters

### curriculumId

`string`

The curriculum identifier.

### moduleId

`string`

The module identifier.

### eventId

`string` \| `null`

The event identifier (or null if reordering a module mapping).

### dayId

`string`

The day identifier.

### newSortOrder

`number`

The new sort order weight.

## Returns

`Promise`\<`RowList`\<`never`[]\>\>

The database update operation result.
