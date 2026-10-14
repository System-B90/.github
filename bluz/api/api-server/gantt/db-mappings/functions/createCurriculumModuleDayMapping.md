[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-mappings](../index.md) / createCurriculumModuleDayMapping

# Function: createCurriculumModuleDayMapping()

> **createCurriculumModuleDayMapping**(`data`, `executor?`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-mappings.ts:74](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-server/gantt/db-mappings.ts#L74)

Creates a new module or event day mapping.

## Parameters

### data

The details for the new mapping.

#### allottedMinutes?

`number`

Defaults to the event's whole duration: placing an event allots it in full.

#### curriculumId

`string`

#### dayId

`string`

#### eventId?

`string` \| `null`

#### moduleId

`string`

#### sortOrder?

`number`

#### weekOnly?

`boolean`

Placed for the week rather than this exact day (#964).

### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md) = `postgresDb`

## Returns

`Promise`\<`object`[]\>

The created mapping record.
