[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/course-tree](../index.md) / relatedCoursesResolver

# Function: relatedCoursesResolver()

> **relatedCoursesResolver**(`courses`): (`courseIds`) => `Set`\<`string`\>

Defined in: [ui/src/api-shared/course-tree.ts:58](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/course-tree.ts#L58)

`relatedCourses` with the tree indexed once and each course's closure
cached, for callers resolving many id sets against the same course list.

## Parameters

### courses

`Pick`\<[`Course`](../../types/course/type-aliases/Course.md), `"id"` \| `"parentId"`\>[]

## Returns

(`courseIds`) => `Set`\<`string`\>
