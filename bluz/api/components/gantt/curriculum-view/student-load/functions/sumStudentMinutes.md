[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / sumStudentMinutes

# Function: sumStudentMinutes()

> **sumStudentMinutes**(`byDay`, `dayIds`, `pathId?`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:539](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/gantt/curriculum-view/student-load.ts#L539)

Scheduled minutes over a set of days: each path's total, and the busiest
path's. A student's week is the sum of their days, not of the busiest days.
With `pathId`, that one path's total instead of the busiest (#899).

## Parameters

### byDay

`Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), [`DayStudentLoad`](../type-aliases/DayStudentLoad.md)\>

### dayIds

`Iterable`\<`string`\>

### pathId?

`string` \| `null`

## Returns

`number`
