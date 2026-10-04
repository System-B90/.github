[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / hasConflictingTemporalConstraints

# Function: hasConflictingTemporalConstraints()

> **hasConflictingTemporalConstraints**(`constraints`): `boolean`

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:119](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/gantt/models/constraint.ts#L119)

Detects mutually conflicting temporal constraints (issue #104): intersects
all `allowedDays`, subtracts all `forbiddenDays`, and reports a conflict
when no valid day of the week remains. Warning-level only — saving is
never blocked by this check.

## Parameters

### constraints

([`GanttConstraint`](../type-aliases/GanttConstraint.md) \| `undefined`)[]

## Returns

`boolean`
