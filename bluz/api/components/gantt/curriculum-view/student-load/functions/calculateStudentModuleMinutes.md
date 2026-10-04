[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / calculateStudentModuleMinutes

# Function: calculateStudentModuleMinutes()

> **calculateStudentModuleMinutes**(`moduleId`, `state`, `courses`, `occurrenceCtx?`, `ignoreBreaks?`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:567](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/student-load.ts#L567)

One student's minimum time in a module, recurring events per occurrence.

## Parameters

### moduleId

`string`

### state

[`NormalizedStore`](../../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### courses

[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)[]

### occurrenceCtx?

[`RecurrenceOccurrenceContext`](../../../utils/type-aliases/RecurrenceOccurrenceContext.md)

### ignoreBreaks?

`boolean` = `false`

## Returns

`number`
