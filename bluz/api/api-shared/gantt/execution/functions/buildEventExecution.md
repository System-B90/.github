[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/execution](../index.md) / buildEventExecution

# Function: buildEventExecution()

> **buildEventExecution**(`args`): [`GanttEventExecution`](../../../types/gantt/execution/type-aliases/GanttEventExecution.md)

Defined in: [ui/src/api-shared/gantt/execution.ts:46](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/execution.ts#L46)

Joins one gantt event's planned occurrences with its cut schedule events.

## Parameters

### args

#### ganttEventId

`string`

#### plannedInstructorIds

`number`[]

#### plannedOccurrences

[`PlannedOccurrence`](../../cut-planner/type-aliases/PlannedOccurrence.md)[]

#### scheduleEvents

[`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)[]

All cut events for this gantt event, including archived ones.

## Returns

[`GanttEventExecution`](../../../types/gantt/execution/type-aliases/GanttEventExecution.md)
