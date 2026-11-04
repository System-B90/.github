[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/hive-lesson-check](../index.md) / unmatchedCoursesResolver

# Function: unmatchedCoursesResolver()

> **unmatchedCoursesResolver**(`courses`, `hiveClasses`): (`courseIds`) => `string`[]

Defined in: [ui/src/components/schedule/hive-lesson-check.ts:42](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/hive-lesson-check.ts#L42)

Indexes the course tree and Hive's groups once, for checking many events.

## Parameters

### courses

`Pick`\<[`Course`](../../../../api-shared/types/course/type-aliases/Course.md), `"id"` \| `"name"` \| `"parentId"` \| `"hiveClassId"`\>[]

Bluz courses.

### hiveClasses

`Class`[]

Hive student groups.

## Returns

Course ids → names of those whose whole subtree has no Hive group.

(`courseIds`) => `string`[]
