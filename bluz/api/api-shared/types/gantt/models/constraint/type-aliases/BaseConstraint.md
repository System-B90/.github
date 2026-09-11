[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / BaseConstraint

# Type Alias: BaseConstraint

> **BaseConstraint** = \{ `id`: `string`; `ownerEventId`: [`GanttEventId`](../../event/type-aliases/GanttEventId.md); `ownerModuleId?`: [`GanttModuleId`](../../module/type-aliases/GanttModuleId.md); `ownerType`: `"event"`; `type`: [`ConstraintType`](../enumerations/ConstraintType.md); \} \| \{ `id`: `string`; `ownerEventId?`: [`GanttEventId`](../../event/type-aliases/GanttEventId.md); `ownerModuleId`: [`GanttModuleId`](../../module/type-aliases/GanttModuleId.md); `ownerType`: `"module"`; `type`: [`ConstraintType`](../enumerations/ConstraintType.md); \}

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:12](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/models/constraint.ts#L12)
