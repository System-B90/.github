[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/types](../index.md) / GanttConstraintState

# Type Alias: GanttConstraintState

> **GanttConstraintState** = `object`

Defined in: [ui/src/components/gantt/state/constraints/types.ts:6](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/state/constraints/types.ts#L6)

State representation for the Gantt constraints context provider.

## Properties

### constraints

> **constraints**: `Record`\<`string`, [`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)\>

Defined in: [ui/src/components/gantt/state/constraints/types.ts:8](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/state/constraints/types.ts#L8)

Map of constraint IDs to their constraint records.

***

### isLoading

> **isLoading**: `boolean`

Defined in: [ui/src/components/gantt/state/constraints/types.ts:11](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/state/constraints/types.ts#L11)

Flag indicating if the constraints are currently loading.
