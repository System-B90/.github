[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutDecision

# Type Alias: CutDecision

> **CutDecision** = \{ `proposals`: [`ConstraintMoveProposal`](../../cut-constraints/type-aliases/ConstraintMoveProposal.md)[]; `type`: `"constraint-moves"`; \} \| \{ `type`: `"constraint-violation"`; `violation`: [`ConstraintViolation`](../../cut-constraints/type-aliases/ConstraintViolation.md); \} \| \{ `excessMinutes`: `number`; `overloadedDays`: `object`[]; `type`: `"week-overflow"`; `weekId`: `string`; `weekNumber`: `number`; \}

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:203](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/gantt/cut-planner.ts#L203)

A question the cut could not answer on its own. The dialog walks these one at
a time rather than presenting a switchboard, and sends the answers back with
the commit. See `docs/gantt-cut-rules.md`.

## Union Members

### Type Literal

\{ `proposals`: [`ConstraintMoveProposal`](../../cut-constraints/type-aliases/ConstraintMoveProposal.md)[]; `type`: `"constraint-moves"`; \}

***

### Type Literal

\{ `type`: `"constraint-violation"`; `violation`: [`ConstraintViolation`](../../cut-constraints/type-aliases/ConstraintViolation.md); \}

***

### Type Literal

\{ `excessMinutes`: `number`; `overloadedDays`: `object`[]; `type`: `"week-overflow"`; `weekId`: `string`; `weekNumber`: `number`; \}

#### excessMinutes

> **excessMinutes**: `number`

#### overloadedDays

> **overloadedDays**: `object`[]

#### type

> **type**: `"week-overflow"`

#### weekId

> **weekId**: `string`

#### weekNumber

> **weekNumber**: `number`

1-based week number, for the Hebrew prompt.
