[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/context](../index.md) / ConstraintsByEventContext

# Variable: ConstraintsByEventContext

> `const` **ConstraintsByEventContext**: `Context`\<`Record`\<`string`, [`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]\> \| `undefined`\>

Defined in: [ui/src/components/gantt/state/constraints/context.ts:72](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/gantt/state/constraints/context.ts#L72)

Constraints binding each event of the open curriculum — its own plus its
modules'. Curriculum-wide and never shadowed by the dialogs' scoped
providers, so load and occurrence counts see every weekday restriction.
