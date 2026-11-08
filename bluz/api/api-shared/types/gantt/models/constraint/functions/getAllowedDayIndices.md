[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / getAllowedDayIndices

# Function: getAllowedDayIndices()

> **getAllowedDayIndices**(`constraints`): `Set`\<[`GanttDayIndex`](../../day/enumerations/GanttDayIndex.md)\> \| `null`

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:111](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types/gantt/models/constraint.ts#L111)

Weekdays a set of temporal constraints permits: intersects every
`allowedDays`, then subtracts every `forbiddenDays`. `null` means
unrestricted (no temporal constraints) — recurrence echoing and other
callers should skip filtering entirely rather than treat it as "no days
allowed".

## Parameters

### constraints

([`GanttConstraint`](../type-aliases/GanttConstraint.md) \| `undefined`)[] \| `undefined`

## Returns

`Set`\<[`GanttDayIndex`](../../day/enumerations/GanttDayIndex.md)\> \| `null`
