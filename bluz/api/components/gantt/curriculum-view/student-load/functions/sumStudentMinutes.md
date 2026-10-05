[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / sumStudentMinutes

# Function: sumStudentMinutes()

> **sumStudentMinutes**(`byDay`, `dayIds`, `pathId?`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:481](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/student-load.ts#L481)

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
