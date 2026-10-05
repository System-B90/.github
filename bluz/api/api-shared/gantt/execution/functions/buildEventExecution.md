[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/execution](../index.md) / buildEventExecution

# Function: buildEventExecution()

> **buildEventExecution**(`args`): [`GanttEventExecution`](../../../types/gantt/execution/type-aliases/GanttEventExecution.md)

Defined in: [ui/src/api-shared/gantt/execution.ts:46](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/gantt/execution.ts#L46)

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
