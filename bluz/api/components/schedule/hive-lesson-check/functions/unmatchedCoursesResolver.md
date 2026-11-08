[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/hive-lesson-check](../index.md) / unmatchedCoursesResolver

# Function: unmatchedCoursesResolver()

> **unmatchedCoursesResolver**(`courses`, `hiveClasses`): (`courseIds`) => `string`[]

Defined in: [ui/src/components/schedule/hive-lesson-check.ts:42](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/hive-lesson-check.ts#L42)

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
