[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/execution](../index.md) / ApiCurriculumExecutionResponse

# Type Alias: ApiCurriculumExecutionResponse

> **ApiCurriculumExecutionResponse** = `object`

Defined in: [ui/src/api-shared/types/gantt/execution.ts:61](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/execution.ts#L61)

## Properties

### events

> **events**: `Record`\<[`GanttEventId`](../../models/shared/type-aliases/GanttEventId.md), [`GanttEventExecution`](GanttEventExecution.md)\>

Defined in: [ui/src/api-shared/types/gantt/execution.ts:66](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/execution.ts#L66)

Keyed by gantt event id. Only gantt events that were cut appear here;
empty object ⇒ curriculum not cut yet (or no linked iteration).
