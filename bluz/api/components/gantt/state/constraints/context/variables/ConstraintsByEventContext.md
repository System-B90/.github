[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/context](../index.md) / ConstraintsByEventContext

# Variable: ConstraintsByEventContext

> `const` **ConstraintsByEventContext**: `Context`\<`Record`\<`string`, [`GanttConstraint`](../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]\> \| `undefined`\>

Defined in: [ui/src/components/gantt/state/constraints/context.ts:72](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/state/constraints/context.ts#L72)

Constraints binding each event of the open curriculum — its own plus its
modules'. Curriculum-wide and never shadowed by the dialogs' scoped
providers, so load and occurrence counts see every weekday restriction.
