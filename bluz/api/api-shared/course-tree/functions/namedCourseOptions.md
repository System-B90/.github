[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/course-tree](../index.md) / namedCourseOptions

# Function: namedCourseOptions()

> **namedCourseOptions**(`courseIds`, `courses`): `Set`\<`string`\>

Defined in: [ui/src/api-shared/course-tree.ts:225](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/course-tree.ts#L225)

The courses a day's events offer as filter options on the student board
(#1027): every course an event names, plus the courses above it. Shuffles
are offered only when an event names them outright — a course never offers
its shuffles, nor a shuffle its siblings. Unknown ids are dropped; cycles
are safe.

## Parameters

### courseIds

`Iterable`\<`string`\>

### courses

`Pick`\<[`Course`](../../types/course/type-aliases/Course.md), `"id"` \| `"description"` \| `"parentId"`\>[]

## Returns

`Set`\<`string`\>
