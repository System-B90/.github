[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-constraints](../index.md) / ConstraintEntity

# Type Alias: ConstraintEntity

> **ConstraintEntity** = `object`

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-constraints.ts#L31)

Constraint pass for the cut.

Two jobs, both governed by `CONSTRAINT_RULES` in `cut-rules.ts`:

1. **Reorder within a day** so a dependent event follows its "after" target
   when both landed on the same day. Free — nothing moves between days, so
   this is applied silently.
2. **Solve across days** — propose moving an event to a different day in the
   same week so a relational or temporal constraint is satisfied. These are
   never applied silently: they surface as proposals the dialog asks the user
   to accept or reject, because the user mapped those days deliberately.

Capacity outranks constraints (`capacityOutranksConstraints`): a proposal
that would push a day past its working window is discarded before it is ever
shown, since the cut may not place anything outside working hours.

Cross-week moves are deliberately out of scope — a constraint that can only
be satisfied by moving between weeks is reported as a violation instead.

## Properties

### constraints

> **constraints**: [`GanttConstraint`](../../../types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-constraints.ts#L35)

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:33](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-constraints.ts#L33)

Event id, or module id for a module-owned constraint.

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:34](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-constraints.ts#L34)
