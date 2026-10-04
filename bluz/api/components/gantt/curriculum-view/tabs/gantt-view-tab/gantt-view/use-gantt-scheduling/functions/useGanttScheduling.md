[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-scheduling](../index.md) / useGanttScheduling

# Function: useGanttScheduling()

> **useGanttScheduling**(`__namedParameters`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-scheduling.ts:13](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-gantt-scheduling.ts#L13)

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

### scheduledMinutesByDay

> **scheduledMinutesByDay**: `Record`\<`string`, `number`\>

### studentLoadByDay

> **studentLoadByDay**: `Record`\<`string`, [`DayStudentLoad`](../../../../../student-load/type-aliases/DayStudentLoad.md)\>

### studentPaths

> **studentPaths**: [`StudentPath`](../../../../../student-load/type-aliases/StudentPath.md)[] = `schedule.paths`
