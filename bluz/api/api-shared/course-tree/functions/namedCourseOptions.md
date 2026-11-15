[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/course-tree](../index.md) / namedCourseOptions

# Function: namedCourseOptions()

> **namedCourseOptions**(`courseIds`, `courses`): `Set`\<`string`\>

Defined in: [ui/src/api-shared/course-tree.ts:225](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-shared/course-tree.ts#L225)

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
