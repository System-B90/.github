[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-violations](../index.md) / temporalViolationsAt

# Function: temporalViolationsAt()

> **temporalViolationsAt**(`constraints`, `dayIndex`): `string`[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-violations.ts:16](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-violations.ts#L16)

The temporal rules a placement on `dayIndex` would break. Shared by the
after-the-fact flags below and the pre-drop warning (#811).

## Parameters

### constraints

readonly ([`GanttConstraint`](../../../../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md) \| `undefined`)[]

### dayIndex

[`GanttDayIndex`](../../../../../../../../api-shared/types/gantt/models/day/enumerations/GanttDayIndex.md)

## Returns

`string`[]
