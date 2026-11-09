[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-groups](../index.md) / findCourseHiveGroup

# Function: findCourseHiveGroup()

> **findCourseHiveGroup**\<`T`\>(`course`, `groups`): `T` \| `undefined`

Defined in: [ui/src/api-shared/hive-groups.ts:11](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/hive-groups.ts#L11)

The Hive student group a Bluz course (a shuffle) syncs against: its
explicitly linked group when set (#774), else the group with its name.
Names compare normalized (trimmed, inner spaces collapsed), the way the
Gantt matches shuffles, so a group that looks linked there is linked here.

## Type Parameters

### T

`T` *extends* `Pick`\<`Class`, `"id"` \| `"name"`\>

## Parameters

### course

`Pick`\<[`Course`](../../types/course/type-aliases/Course.md), `"hiveClassId"` \| `"name"`\>

### groups

`T`[]

## Returns

`T` \| `undefined`
