[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / calculateStudentTentativeMinutes

# Function: calculateStudentTentativeMinutes()

> **calculateStudentTentativeMinutes**(`__namedParameters`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:673](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/curriculum-view/student-load.ts#L673)

One student's time in the modules placed whole (tentatively) on the
timeline, each module counted once however many days it is mapped to.

## Parameters

### \_\_namedParameters

#### courses

[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)[]

#### mappings

`Record`\<`string`, [`GanttCurriculumEventDayMapping`](../../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

#### moduleIds

`Iterable`\<`string`\>

#### state

[`NormalizedStore`](../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

## Returns

`number`
