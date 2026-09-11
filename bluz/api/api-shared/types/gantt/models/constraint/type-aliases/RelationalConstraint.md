[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / RelationalConstraint

# Type Alias: RelationalConstraint

> **RelationalConstraint** = [`BaseConstraint`](BaseConstraint.md) & `object`

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/models/constraint.ts#L31)

Handles dependencies between two entities (Event-Event, Module-Module, Mixed).

## Type Declaration

### maxDelayDays?

> `optional` **maxDelayDays?**: `number`

### minDelayDays?

> `optional` **minDelayDays?**: `number`

### relation

> **relation**: `"after"` \| `"before"`

### targetId

> **targetId**: [`GanttEventId`](../../event/type-aliases/GanttEventId.md) \| [`GanttModuleId`](../../module/type-aliases/GanttModuleId.md)

### targetType

> **targetType**: [`EntityType`](EntityType.md)

### type

> **type**: [`Relational`](../enumerations/ConstraintType.md#relational)
