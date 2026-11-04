[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-courses](../../../index.md) / [DbCourses](../index.md) / create

# Variable: create

> `const` **create**: (`course`, `controller`) => `Promise`\<`Pick`\<[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md), `"id"` \| `"name"` \| `"description"` \| `"color"` \| `"parentId"` \| `"hiveClassId"` \| `"instructorIds"`\>\> = `createDbCourse`

Defined in: [ui/src/api-server/db-courses.ts:88](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/db-courses.ts#L88)

## Parameters

### course

[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

## Returns

`Promise`\<`Pick`\<[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md), `"id"` \| `"name"` \| `"description"` \| `"color"` \| `"parentId"` \| `"hiveClassId"` \| `"instructorIds"`\>\>
