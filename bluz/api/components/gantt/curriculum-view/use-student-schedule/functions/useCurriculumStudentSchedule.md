[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/use-student-schedule](../index.md) / useCurriculumStudentSchedule

# Function: useCurriculumStudentSchedule()

> **useCurriculumStudentSchedule**(`curriculum`, `state`): [`CurriculumStudentSchedule`](../type-aliases/CurriculumStudentSchedule.md)

Defined in: [ui/src/components/gantt/curriculum-view/use-student-schedule.ts:37](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/curriculum-view/use-student-schedule.ts#L37)

The curriculum's schedule as a single student lives it, over the whole
timeline: every view that shows scheduled time reads it from here, so the
timeline, weeks grid and summaries always agree.

## Parameters

### curriculum

[`GanttCurriculum`](../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md) \| `undefined`

### state

[`NormalizedStore`](../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

## Returns

[`CurriculumStudentSchedule`](../type-aliases/CurriculumStudentSchedule.md)
