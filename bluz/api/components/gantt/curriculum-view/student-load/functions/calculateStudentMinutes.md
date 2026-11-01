[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / calculateStudentMinutes

# Function: calculateStudentMinutes()

> **calculateStudentMinutes**(`args`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:628](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/gantt/curriculum-view/student-load.ts#L628)

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
