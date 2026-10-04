[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/types](../index.md) / GanttConstraintAction

# Type Alias: GanttConstraintAction

> **GanttConstraintAction** = \{ `payload`: \{ `id`: `string`; \}; `type`: `"DELETE_CONSTRAINT"`; \} \| \{ `payload`: [`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]; `type`: `"SET_CONSTRAINTS"`; \} \| \{ `payload`: `boolean`; `type`: `"SET_LOADING"`; \} \| \{ `payload`: [`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md); `type`: `"UPSERT_CONSTRAINT"`; \}

Defined in: [ui/src/components/gantt/state/constraints/types.ts:17](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/state/constraints/types.ts#L17)

Action definitions for the Gantt constraints context state reducer.
