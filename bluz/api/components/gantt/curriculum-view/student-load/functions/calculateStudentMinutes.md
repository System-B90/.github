[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / calculateStudentMinutes

# Function: calculateStudentMinutes()

> **calculateStudentMinutes**(`args`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:560](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/student-load.ts#L560)

`calculateStudentMinutesByPath`'s busiest path — one student's time.

## Parameters

### args

#### courses

[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)[]

#### include?

(`eventId`, `moduleId`) => `boolean`

#### occurrenceCtx?

[`RecurrenceOccurrenceContext`](../../../utils/type-aliases/RecurrenceOccurrenceContext.md)

#### state

[`NormalizedStore`](../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

#### syllabusIds

`string`[]

## Returns

`number`
