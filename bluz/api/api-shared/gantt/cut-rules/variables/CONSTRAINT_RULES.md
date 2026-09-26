[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / CONSTRAINT\_RULES

# Variable: CONSTRAINT\_RULES

> `const` **CONSTRAINT\_RULES**: `object`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:380](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-rules.ts#L380)

How the cut treats `GanttConstraint`s (relational after/before with optional
min/max day delays, and temporal allowed/forbidden weekdays).

The cut runs a full solver pass, but never applies a cross-day move silently:
moves the user did not ask for surface as a `constraint-moves` decision the
dialog asks them to accept or reject. Unsatisfiable constraints surface as a
`constraint-violation` decision rather than blocking the cut.

## Type Declaration

### capacityOutranksConstraints

> `readonly` **capacityOutranksConstraints**: `true` = `true`

Capacity outranks constraints: a solver move is rejected outright when
it would place an event outside a day's working window.

### maxSolverPasses

> `readonly` **maxSolverPasses**: `8` = `8`

Iteration cap for the solver. Constraint graphs here are small; the cap
exists so a cyclic graph terminates instead of spinning.

### promptBeforeApplyingMoves

> `readonly` **promptBeforeApplyingMoves**: `true` = `true`

Ask before committing solver-initiated cross-day moves.

### reorderWithinDay

> `readonly` **reorderWithinDay**: `true` = `true`

Reorder events inside a day so an "after" target precedes its dependent.

### solveAcrossDays

> `readonly` **solveAcrossDays**: `true` = `true`

Move events across days (same week) to satisfy constraints.
