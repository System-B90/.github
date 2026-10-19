[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / buildScheduleEvent

# Function: buildScheduleEvent()

> **buildScheduleEvent**(`occurrence`, `ganttEvent`, `courseIds`, `moduleHiveIds`, `hiveModuleSubjectById`, `curriculumId`, `naming?`): [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

Defined in: [ui/src/api-server/gantt/cut.ts:606](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/cut.ts#L606)

## Parameters

### occurrence

[`PlannedOccurrence`](../../../../api-shared/gantt/cut-planner/type-aliases/PlannedOccurrence.md)

### ganttEvent

[`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)

### courseIds

`string`[]

### moduleHiveIds

`number`[]

### hiveModuleSubjectById

`Map`\<`number`, `number`\>

### curriculumId

`string`

### naming?

#### syllabus

[`SyllabusNaming`](../type-aliases/SyllabusNaming.md) \| `undefined`

#### symbolBySubjectId

`Map`\<`number`, `string`\>

## Returns

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)
