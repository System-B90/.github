[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / indexCurriculumEvents

# Function: indexCurriculumEvents()

> **indexCurriculumEvents**(`curriculum`): `object`

Defined in: [ui/src/api-server/gantt/cut.ts:214](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-server/gantt/cut.ts#L214)

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

### syllabusNamingByEvent

> **syllabusNamingByEvent**: `Map`\<`string`, [`SyllabusNaming`](../type-aliases/SyllabusNaming.md)\>

The owning syllabus's naming inputs, per event (#965).

### syllabusTitleByEvent

> **syllabusTitleByEvent**: `Map`\<`string`, `string`\>
