[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/types](../index.md) / GanttConstraintAction

# Type Alias: GanttConstraintAction

> **GanttConstraintAction** = \{ `payload`: \{ `id`: `string`; \}; `type`: `"DELETE_CONSTRAINT"`; \} \| \{ `payload`: [`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]; `type`: `"SET_CONSTRAINTS"`; \} \| \{ `payload`: `boolean`; `type`: `"SET_LOADING"`; \} \| \{ `payload`: [`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md); `type`: `"UPSERT_CONSTRAINT"`; \}

Defined in: [ui/src/components/gantt/state/constraints/types.ts:17](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/state/constraints/types.ts#L17)

Action definitions for the Gantt constraints context state reducer.
