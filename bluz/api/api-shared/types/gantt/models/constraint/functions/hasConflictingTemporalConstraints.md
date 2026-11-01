[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / hasConflictingTemporalConstraints

# Function: hasConflictingTemporalConstraints()

> **hasConflictingTemporalConstraints**(`constraints`): `boolean`

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:158](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/gantt/models/constraint.ts#L158)

Detects mutually conflicting temporal constraints (issue #104): intersects
all `allowedDays`, subtracts all `forbiddenDays`, and reports a conflict
when no valid day of the week remains. Warning-level only — saving is
never blocked by this check.

## Parameters

### constraints

([`GanttConstraint`](../type-aliases/GanttConstraint.md) \| `undefined`)[]

## Returns

`boolean`
