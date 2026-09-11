[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / indexCurriculumEvents

# Function: indexCurriculumEvents()

> **indexCurriculumEvents**(`curriculum`): `object`

Defined in: [ui/src/api-server/gantt/cut.ts:203](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/cut.ts#L203)

Walk the full curriculum tree once, indexing every event by id and recording
the title of the syllabus each event lives under (used as course provenance).

## Parameters

### curriculum

[`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)

## Returns

### eventIdsByModule

> **eventIdsByModule**: `Map`\<`string`, `string`[]\>

Module id → its event ids, for fanning out module-level constraints.

### eventsById

> **eventsById**: `Map`\<`string`, [`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)\>

### moduleHiveIdsByEvent

> **moduleHiveIdsByEvent**: `Map`\<`string`, `number`[]\>

### moduleIdByEvent

> **moduleIdByEvent**: `Map`\<`string`, `string`\>

Owning gantt module id per event — spillover keeps a module together.

### moduleTitleById

> **moduleTitleById**: `Map`\<`string`, `string`\>

Module titles, used in constraint-violation messages.

### syllabusIdByEvent

> **syllabusIdByEvent**: `Map`\<`string`, `string`\>

Owning syllabus id per event — drives the between-syllabuses break rule.

### syllabusTitleByEvent

> **syllabusTitleByEvent**: `Map`\<`string`, `string`\>
