[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / calculateStudentMinutesByPath

# Function: calculateStudentMinutesByPath()

> **calculateStudentMinutesByPath**(`__namedParameters`): `object`[]

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:525](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/student-load.ts#L525)

The time each kind of student spends in the given syllabuses' events: per
path, each syllabus at its longest shuffle plus the course-limited events
on that path. Recurring events count per occurrence when `occurrenceCtx` is
given. `include` narrows the events counted (a module, the placed
events…) without changing who the students are.

## Parameters

### \_\_namedParameters

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

`object`[]
