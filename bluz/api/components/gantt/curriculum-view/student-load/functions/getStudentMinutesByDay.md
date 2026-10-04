[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / getStudentMinutesByDay

# Function: getStudentMinutesByDay()

> **getStudentMinutesByDay**(`byDay`): `Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), `number`\>

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:510](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/student-load.ts#L510)

Per-day busiest-path minutes, the shape the capacity views consume.

## Parameters

### byDay

`Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), [`DayStudentLoad`](../type-aliases/DayStudentLoad.md)\>

## Returns

`Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), `number`\>
