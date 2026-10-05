[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/course-tree](../index.md) / lowestCommonCourse

# Function: lowestCommonCourse()

> **lowestCommonCourse**(`courseIds`, `courses`): `string` \| `null`

Defined in: [ui/src/api-shared/course-tree.ts:10](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/course-tree.ts#L10)

The deepest existing course that is (or contains) every course in
`courseIds` — the parent a shuffle's new course belongs under. A shuffle
whose syllabus sits only in Apollo lands under Apollo; one spread over Apollo
and Mivtzar lands under their shared parent. Null (top level) when no course
is given or the courses share no ancestor. Ids of unknown courses are ignored.

## Parameters

### courseIds

`Iterable`\<`string`\>

### courses

`Pick`\<[`Course`](../../types/course/type-aliases/Course.md), `"id"` \| `"parentId"`\>[]

## Returns

`string` \| `null`
