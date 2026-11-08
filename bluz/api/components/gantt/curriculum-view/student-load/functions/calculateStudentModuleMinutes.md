[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/student-load](../index.md) / calculateStudentModuleMinutes

# Function: calculateStudentModuleMinutes()

> **calculateStudentModuleMinutes**(`moduleId`, `state`, `courses`, `occurrenceCtx?`, `ignoreBreaks?`): `number`

Defined in: [ui/src/components/gantt/curriculum-view/student-load.ts:636](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/gantt/curriculum-view/student-load.ts#L636)

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
