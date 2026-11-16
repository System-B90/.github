[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/hive-lesson-check](../index.md) / unmatchedCoursesResolver

# Function: unmatchedCoursesResolver()

> **unmatchedCoursesResolver**(`courses`, `hiveClasses`): (`courseIds`) => `string`[]

Defined in: [ui/src/components/schedule/hive-lesson-check.ts:42](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/schedule/hive-lesson-check.ts#L42)

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
