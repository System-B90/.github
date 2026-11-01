[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / calculateStudentModuleMinutes

# Function: calculateStudentModuleMinutes()

> **calculateStudentModuleMinutes**(`moduleId`, `state`, `courses`, `occurrenceCtx?`, `ignoreBreaks?`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:636](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/gantt/curriculum-view/student-load.ts#L636)

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
