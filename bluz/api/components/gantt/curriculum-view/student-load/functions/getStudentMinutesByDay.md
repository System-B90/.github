[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / getStudentMinutesByDay

# Function: getStudentMinutesByDay()

> **getStudentMinutesByDay**(`byDay`): `Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), `number`\>

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:510](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/curriculum-view/student-load.ts#L510)

Per-day busiest-path minutes, the shape the capacity views consume.

## Parameters

### byDay

`Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), [`DayStudentLoad`](../type-aliases/DayStudentLoad.md)\>

## Returns

`Record`\<[`GanttDayId`](../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md), `number`\>
