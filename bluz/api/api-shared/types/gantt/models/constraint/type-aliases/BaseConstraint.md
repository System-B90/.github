[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / BaseConstraint

# Type Alias: BaseConstraint

> **BaseConstraint** = \{ `id`: `string`; `ownerEventId`: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md); `ownerModuleId?`: [`GanttModuleId`](../../shared/type-aliases/GanttModuleId.md); `ownerType`: `"event"`; `type`: [`ConstraintType`](../enumerations/ConstraintType.md); \} \| \{ `id`: `string`; `ownerEventId?`: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md); `ownerModuleId`: [`GanttModuleId`](../../shared/type-aliases/GanttModuleId.md); `ownerType`: `"module"`; `type`: [`ConstraintType`](../enumerations/ConstraintType.md); \}

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:14](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/gantt/models/constraint.ts#L14)
