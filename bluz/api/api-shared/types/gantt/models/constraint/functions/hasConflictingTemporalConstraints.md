[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / hasConflictingTemporalConstraints

# Function: hasConflictingTemporalConstraints()

> **hasConflictingTemporalConstraints**(`constraints`): `boolean`

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:146](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/types/gantt/models/constraint.ts#L146)

Detects mutually conflicting temporal constraints (issue #104): intersects
all `allowedDays`, subtracts all `forbiddenDays`, and reports a conflict
when no valid day of the week remains. Warning-level only — saving is
never blocked by this check.

## Parameters

### constraints

([`GanttConstraint`](../type-aliases/GanttConstraint.md) \| `undefined`)[]

## Returns

`boolean`
