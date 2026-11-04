[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / buildScheduleEvent

# Function: buildScheduleEvent()

> **buildScheduleEvent**(`occurrence`, `ganttEvent`, `courseIds`, `moduleHiveIds`, `hiveModuleSubjectById`, `curriculumId`, `naming?`, `assignInstructors?`): [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

Defined in: [ui/src/api-server/gantt/cut.ts:638](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/cut.ts#L638)

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

### assignInstructors?

`boolean` = `true`

## Returns

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)
