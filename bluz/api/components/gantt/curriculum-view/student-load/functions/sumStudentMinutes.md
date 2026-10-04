[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / sumStudentMinutes

# Function: sumStudentMinutes()

> **sumStudentMinutes**(`byDay`, `dayIds`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:480](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/student-load.ts#L480)

Scheduled minutes over a set of days: each path's total, and the busiest
path's. A student's week is the sum of their days, not of the busiest days.

## Parameters

### byDay

`Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), [`DayStudentLoad`](../type-aliases/DayStudentLoad.md)\>

### dayIds

`Iterable`\<`string`\>

## Returns

`number`
