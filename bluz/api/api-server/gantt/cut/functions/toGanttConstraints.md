[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / toGanttConstraints

# Function: toGanttConstraints()

> **toGanttConstraints**(`rows`): [`GanttConstraint`](../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]

Defined in: [ui/src/api-server/gantt/cut.ts:126](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-server/gantt/cut.ts#L126)

Adapt stored constraint rows into the domain `GanttConstraint` union the
solver consumes. The table is a single flat shape covering both variants, so
a row that does not carry the columns its own type requires (a relational
row with no target, an ownerless row) is dropped rather than fed to the
solver as a half-built constraint.

## Parameters

### rows

[`CutConstraintRow`](../type-aliases/CutConstraintRow.md)[]

## Returns

[`GanttConstraint`](../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]
