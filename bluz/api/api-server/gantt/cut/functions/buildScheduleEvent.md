[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / buildScheduleEvent

# Function: buildScheduleEvent()

> **buildScheduleEvent**(`occurrence`, `ganttEvent`, `courseIds`, `moduleHiveIds`, `hiveModuleSubjectById`, `curriculumId`): [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

Defined in: [ui/src/api-server/gantt/cut.ts:460](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/cut.ts#L460)

Build a single schedule-event document from a planned occurrence and its
source gantt event. Hive linkage is copied when present on the event
itself; when the event has no linkage of its own, it falls back to the
first Hive module linked on its containing Gantt module (via
`hiveModuleSubjectById`), since users commonly link Hive at the module
level (module dialog chips) rather than per-event. Only when neither is
set is the event stored as a non-Hive placeholder (subject/module 0,
lesson null), matching how "fake" events represent "no Hive linkage".

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

## Returns

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)
