[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/course-tree](../index.md) / relatedCourses

# Function: relatedCourses()

> **relatedCourses**(`courseIds`, `courses`): `Set`\<`string`\>

Defined in: [ui/src/api-shared/course-tree.ts:43](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/course-tree.ts#L43)

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
