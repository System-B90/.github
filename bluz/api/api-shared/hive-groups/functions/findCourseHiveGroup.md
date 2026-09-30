[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-groups](../index.md) / findCourseHiveGroup

# Function: findCourseHiveGroup()

> **findCourseHiveGroup**\<`T`\>(`course`, `groups`): `T` \| `undefined`

Defined in: [ui/src/api-shared/hive-groups.ts:8](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/hive-groups.ts#L8)

The Hive student group a Bluz course (a shuffle) syncs against: its
explicitly linked group when set (#774), else the group with its exact name.

## Type Parameters

### T

`T` *extends* `Pick`\<`Class`, `"name"` \| `"id"`\>

## Parameters

### course

`Pick`\<[`Course`](../../types/course/type-aliases/Course.md), `"hiveClassId"` \| `"name"`\>

### groups

`T`[]

## Returns

`T` \| `undefined`
