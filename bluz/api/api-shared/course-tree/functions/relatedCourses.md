[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/course-tree](../index.md) / relatedCourses

# Function: relatedCourses()

> **relatedCourses**(`courseIds`, `courses`): `Set`\<`string`\>

Defined in: [ui/src/api-shared/course-tree.ts:46](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/course-tree.ts#L46)

Every course on the tree path through `courseIds`: the courses themselves,
all their ancestors and all their descendants. An event tagged for a shuffle
concerns the shuffles above it (whose students include it) and below it
(which are part of it). Ids of unknown courses are ignored; cycles are safe.

## Parameters

### courseIds

`Iterable`\<`string`\>

### courses

`Pick`\<[`Course`](../../types/course/type-aliases/Course.md), `"id"` \| `"parentId"`\>[]

## Returns

`Set`\<`string`\>
