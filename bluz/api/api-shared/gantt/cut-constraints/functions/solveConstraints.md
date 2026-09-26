[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-constraints](../index.md) / solveConstraints

# Function: solveConstraints()

> **solveConstraints**(`input`): [`ConstraintPassResult`](../type-aliases/ConstraintPassResult.md)

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:161](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-constraints.ts#L161)

Run the constraint solver over an already-balanced placement map.

Returns proposals (never applied here — the caller decides) and violations.
The pass is idempotent and side-effect free; `maxSolverPasses` bounds it so a
cyclic constraint graph terminates instead of spinning.

## Parameters

### input

[`ConstraintPassInput`](../type-aliases/ConstraintPassInput.md)

## Returns

[`ConstraintPassResult`](../type-aliases/ConstraintPassResult.md)
