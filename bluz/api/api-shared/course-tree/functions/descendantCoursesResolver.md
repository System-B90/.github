[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/course-tree](../index.md) / descendantCoursesResolver

# Function: descendantCoursesResolver()

> **descendantCoursesResolver**(`courses`): (`courseIds`) => `Set`\<`string`\>

Defined in: [ui/src/api-shared/course-tree.ts:126](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/course-tree.ts#L126)

Resolver for `courseIds` plus all their descendants. A break for Bis90 also
reaches Apollo, whose students are part of Bis90 (#974). Unknown ids pass
through unchanged; cycles are safe.

## Parameters

### courses

`Pick`\<[`Course`](../../types/course/type-aliases/Course.md), `"id"` \| `"parentId"`\>[]

## Returns

(`courseIds`) => `Set`\<`string`\>
