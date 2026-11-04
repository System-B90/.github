[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/execution](../index.md) / ApiCurriculumExecutionResponse

# Type Alias: ApiCurriculumExecutionResponse

> **ApiCurriculumExecutionResponse** = `object`

Defined in: [ui/src/api-shared/types/gantt/execution.ts:61](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/gantt/execution.ts#L61)

## Properties

### events

> **events**: `Record`\<[`GanttEventId`](../../models/shared/type-aliases/GanttEventId.md), [`GanttEventExecution`](GanttEventExecution.md)\>

Defined in: [ui/src/api-shared/types/gantt/execution.ts:66](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/gantt/execution.ts#L66)

Keyed by gantt event id. Only gantt events that were cut appear here;
empty object ⇒ curriculum not cut yet (or no linked iteration).
