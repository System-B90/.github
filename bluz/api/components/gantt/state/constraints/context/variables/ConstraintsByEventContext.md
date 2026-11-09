[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/context](../index.md) / ConstraintsByEventContext

# Variable: ConstraintsByEventContext

> `const` **ConstraintsByEventContext**: `Context`\<`Record`\<`string`, [`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]\> \| `undefined`\>

Defined in: [ui/src/components/gantt/state/constraints/context.ts:72](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/gantt/state/constraints/context.ts#L72)

Constraints binding each event of the open curriculum — its own plus its
modules'. Curriculum-wide and never shadowed by the dialogs' scoped
providers, so load and occurrence counts see every weekday restriction.
