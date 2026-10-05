[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/use-student-schedule](../index.md) / useCurriculumStudentSchedule

# Function: useCurriculumStudentSchedule()

> **useCurriculumStudentSchedule**(`curriculum`, `state`): [`CurriculumStudentSchedule`](../type-aliases/CurriculumStudentSchedule.md)

Defined in: [ui/src/components/gantt/curriculum-view/use-student-schedule.ts:36](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/use-student-schedule.ts#L36)

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
