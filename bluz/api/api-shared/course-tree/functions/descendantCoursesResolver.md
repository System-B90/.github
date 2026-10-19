[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/course-tree](../index.md) / descendantCoursesResolver

# Function: descendantCoursesResolver()

> **descendantCoursesResolver**(`courses`): (`courseIds`) => `Set`\<`string`\>

Defined in: [ui/src/api-shared/course-tree.ts:114](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/course-tree.ts#L114)

Resolver for `courseIds` plus all their descendants. A break for Bis90 also
reaches Apollo, whose students are part of Bis90 (#974). Unknown ids pass
through unchanged; cycles are safe.

## Parameters

### courses

`Pick`\<[`Course`](../../types/course/type-aliases/Course.md), `"id"` \| `"parentId"`\>[]

## Returns

(`courseIds`) => `Set`\<`string`\>
