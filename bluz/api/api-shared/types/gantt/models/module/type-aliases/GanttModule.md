[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/module](../index.md) / GanttModule

# Type Alias: GanttModule

> **GanttModule** = `object` & [`BaseGantItem`](../../shared/type-aliases/BaseGantItem.md)

Defined in: [ui/src/api-shared/types/gantt/models/module.ts:9](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/api-shared/types/gantt/models/module.ts#L9)

## Type Declaration

### constraints

> **constraints**: [`GanttConstraint`](../../constraint/type-aliases/GanttConstraint.md)[]

### defaultOrchestratorId

> **defaultOrchestratorId**: `null` \| `number`

Hive id of the instructor new events in this module are pre-filled
with as their orchestrator; null for no default. Existing events are
left untouched when this changes.

### description

> **description**: `string`

### events

> **events**: [`GanttEventId`](../../shared/type-aliases/GanttEventId.md)[]

### hiveIds

> **hiveIds**: `number`[]

### shuffles?

> `optional` **shuffles?**: `string`[]

Shuffle names (from the parent syllabus) this module applies to.
Empty/undefined ⇒ applies to all shuffles.

### title

> **title**: `string`
