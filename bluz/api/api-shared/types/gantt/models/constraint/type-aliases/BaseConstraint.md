[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / BaseConstraint

# Type Alias: BaseConstraint

> **BaseConstraint** = \{ `id`: `string`; `ownerEventId`: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md); `ownerModuleId?`: [`GanttModuleId`](../../shared/type-aliases/GanttModuleId.md); `ownerType`: `"event"`; `type`: [`ConstraintType`](../enumerations/ConstraintType.md); \} \| \{ `id`: `string`; `ownerEventId?`: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md); `ownerModuleId`: [`GanttModuleId`](../../shared/type-aliases/GanttModuleId.md); `ownerType`: `"module"`; `type`: [`ConstraintType`](../enumerations/ConstraintType.md); \}

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:14](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/gantt/models/constraint.ts#L14)
