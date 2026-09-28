[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/constraint](../index.md) / TemporalConstraint

# Type Alias: TemporalConstraint

> **TemporalConstraint** = [`BaseConstraint`](BaseConstraint.md) & `object`

Defined in: [ui/src/api-shared/types/gantt/models/constraint.ts:45](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/gantt/models/constraint.ts#L45)

Handles fixed calendar and day-of-week constraints.

## Type Declaration

### allowedDays?

> `optional` **allowedDays?**: [`GanttDayIndex`](../../day/enumerations/GanttDayIndex.md)[]

### forbiddenDays?

> `optional` **forbiddenDays?**: [`GanttDayIndex`](../../day/enumerations/GanttDayIndex.md)[]

### type

> **type**: [`Temporal`](../enumerations/ConstraintType.md#temporal)
