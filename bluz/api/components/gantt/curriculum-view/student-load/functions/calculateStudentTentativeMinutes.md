[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / calculateStudentTentativeMinutes

# Function: calculateStudentTentativeMinutes()

> **calculateStudentTentativeMinutes**(`__namedParameters`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:602](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/student-load.ts#L602)

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
