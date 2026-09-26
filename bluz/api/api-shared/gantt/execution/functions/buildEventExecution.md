[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/execution](../index.md) / buildEventExecution

# Function: buildEventExecution()

> **buildEventExecution**(`args`): [`GanttEventExecution`](../../../types/gantt/execution/type-aliases/GanttEventExecution.md)

Defined in: [ui/src/api-shared/gantt/execution.ts:46](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/execution.ts#L46)

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
