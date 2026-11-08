[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-scheduling](../index.md) / useGanttScheduling

# Function: useGanttScheduling()

> **useGanttScheduling**(`__namedParameters`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-scheduling.ts:13](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-scheduling.ts#L13)

## Parameters

### \_\_namedParameters

#### curriculum

[`GanttCurriculum`](../../../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md) \| `undefined`

#### ignoreBreaks

`boolean`

Leave break events out of the per-day loads.

#### state

[`NormalizedStore`](../../../../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

## Returns

`object`

### eventSpans

> **eventSpans**: `Record`\<`string`, [`EventDaySpan`](../../../../../gantt-time-utils/type-aliases/EventDaySpan.md)\> = `schedule.spans`

### studentLoadByDay

> **studentLoadByDay**: `Record`\<`string`, [`DayStudentLoad`](../../../../../student-load/type-aliases/DayStudentLoad.md)\>

### studentLoadWithBreaksByDay

> **studentLoadWithBreaksByDay**: `Record`\<`string`, [`DayStudentLoad`](../../../../../student-load/type-aliases/DayStudentLoad.md)\> = `schedule.byDay`

### studentPaths

> **studentPaths**: [`StudentPath`](../../../../../student-load/type-aliases/StudentPath.md)[] = `schedule.paths`
