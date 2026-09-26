[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-mappings](../index.md) / getModuleDayMappingsForCurriculum

# Function: getModuleDayMappingsForCurriculum()

> **getModuleDayMappingsForCurriculum**(`curriculumId`, `filters`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-mappings.ts:24](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-mappings.ts#L24)

Retrieves curriculum module/event day mappings for a specific curriculum.
Can be filtered by dayIds and/or weekIds for partial loading.
weekIds are resolved to dayIds via the week->day junction table,
then combined with any explicit dayIds using AND logic.

## Parameters

### curriculumId

`string`

The curriculum identifier.

### filters

Optional filters for dayIds and weekIds.

#### dayIds?

`string`[]

#### weekIds?

`string`[]

## Returns

`Promise`\<`object`[]\>

An array of mapping records.
