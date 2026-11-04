[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-courses](../../../index.md) / [DbCourses](../index.md) / create

# Variable: create

> `const` **create**: (`course`, `controller`) => `Promise`\<`Pick`\<[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md), `"id"` \| `"name"` \| `"description"` \| `"color"` \| `"parentId"` \| `"hiveClassId"` \| `"instructorIds"`\>\> = `createDbCourse`

Defined in: [ui/src/api-server/db-courses.ts:88](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/db-courses.ts#L88)

## Parameters

### course

[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<`Pick`\<[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md), `"id"` \| `"name"` \| `"description"` \| `"color"` \| `"parentId"` \| `"hiveClassId"` \| `"instructorIds"`\>\>
