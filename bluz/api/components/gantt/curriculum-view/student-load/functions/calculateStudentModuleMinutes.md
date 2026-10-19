[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / calculateStudentModuleMinutes

# Function: calculateStudentModuleMinutes()

> **calculateStudentModuleMinutes**(`moduleId`, `state`, `courses`, `occurrenceCtx?`, `ignoreBreaks?`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:573](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/student-load.ts#L573)

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
