[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / RelationalConstraint

# Type Alias: RelationalConstraint

> **RelationalConstraint** = [`BaseConstraint`](BaseConstraint.md) & `object`

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:33](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/models/constraint.ts#L33)

Handles dependencies between two entities (Event-Event, Module-Module, Mixed).

## Type Declaration

### maxDelayDays?

> `optional` **maxDelayDays?**: `number`

### minDelayDays?

> `optional` **minDelayDays?**: `number`

### relation

> **relation**: `"after"` \| `"before"`

### targetId

> **targetId**: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md) \| [`GanttModuleId`](../../shared/type-aliases/GanttModuleId.md)

### targetType

> **targetType**: [`EntityType`](EntityType.md)

### type

> **type**: [`Relational`](../enumerations/ConstraintType.md#relational)
