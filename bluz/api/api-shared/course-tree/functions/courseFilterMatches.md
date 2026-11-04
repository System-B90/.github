[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/course-tree](../index.md) / courseFilterMatches

# Function: courseFilterMatches()

> **courseFilterMatches**(`picked`, `courses`): `Set`\<`string`\>

Defined in: [ui/src/api-shared/course-tree.ts:179](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/course-tree.ts#L179)

Courses whose events a course filter shows. Each picked course matches its
ancestors too: their events apply to its students. Child courses do not
(#963) — filtering Bis90 shows only what all of Bis90 attends.

A picked course that is not itself a shuffle also matches the shuffles
hanging off it or off any of those ancestors (#1030): a shuffle sits under
its syllabus' courses, so its events are theirs. A picked shuffle pulls in
no sibling shuffles. Ids of unknown courses match only themselves.

## Parameters

### picked

`Iterable`\<`string`\>

### courses

`Pick`\<[`Course`](../../types/course/type-aliases/Course.md), `"id"` \| `"description"` \| `"parentId"`\>[]

## Returns

`Set`\<`string`\>
