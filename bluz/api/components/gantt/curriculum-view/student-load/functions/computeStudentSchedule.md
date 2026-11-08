[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / computeStudentSchedule

# Function: computeStudentSchedule()

> **computeStudentSchedule**(`__namedParameters`): [`StudentSchedule`](../type-aliases/StudentSchedule.md)

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:500](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/gantt/curriculum-view/student-load.ts#L500)

Lays out every mapped event (spillover by what its own students have left
on a day) and totals each day per student path. Recurring events count as
if materialized on every occurrence, and are placed before anything spills.

## Parameters

### \_\_namedParameters

#### constraintsByEvent

`Record`\<`string`, [`GanttConstraint`](../../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]\>

#### courses

[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)[]

#### dateOf?

(`dayId`) => `string` \| `undefined`

Calendar date of a day, for recurrence windows (#468).

#### exceptions

`Record`\<`string`, [`GanttEventRecurrenceException`](../../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)\>

#### linearDays

`string`[]

#### mappings

`Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

#### state

[`NormalizedStore`](../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

#### syllabusIds

`string`[]

## Returns

[`StudentSchedule`](../type-aliases/StudentSchedule.md)
