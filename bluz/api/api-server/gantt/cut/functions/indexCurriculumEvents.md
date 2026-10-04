[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / indexCurriculumEvents

# Function: indexCurriculumEvents()

> **indexCurriculumEvents**(`curriculum`): `object`

Defined in: [ui/src/api-server/gantt/cut.ts:210](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/cut.ts#L210)

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

### hiveGroupByShuffle

> **hiveGroupByShuffle**: `Map`\<`string`, `number`\>

Shuffle name → the Hive student group its syllabus links it to (#774).

### moduleHiveIdsByEvent

> **moduleHiveIdsByEvent**: `Map`\<`string`, `number`[]\>

### moduleIdByEvent

> **moduleIdByEvent**: `Map`\<`string`, `string`\>

Owning gantt module id per event — spillover keeps a module together.

### moduleTitleById

> **moduleTitleById**: `Map`\<`string`, `string`\>

Module titles, used in constraint-violation messages.

### shufflesByEvent

> **shufflesByEvent**: `Map`\<`string`, `string`[]\>

Shuffles each event runs for: its own, else its module's, else its
syllabus's. Empty when none is set anywhere up the chain.

### syllabusCourseIdsByEvent

> **syllabusCourseIdsByEvent**: `Map`\<`string`, `string`[]\>

Courses (מסלולים) the owning syllabus is assigned to, per event.

### syllabusIdByEvent

> **syllabusIdByEvent**: `Map`\<`string`, `string`\>

Owning syllabus id per event — drives the between-syllabuses break rule.

### syllabusTitleByEvent

> **syllabusTitleByEvent**: `Map`\<`string`, `string`\>
