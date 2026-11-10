[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-groups](../index.md) / memberCourseIds

# Function: memberCourseIds()

> **memberCourseIds**\<`T`\>(`courses`, `memberOf`, `groups`): `string`[]

Defined in: [ui/src/api-shared/hive-groups.ts:38](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/hive-groups.ts#L38)

The courses a Hive user belongs to: those whose student group (by the same
rule as `findCourseHiveGroup`) is one of the user's groups. A course linked
by `hiveClassId` to one of them counts even when `groups` is empty — a
caller Hive will not let list groups still resolves its explicit links.

## Type Parameters

### T

`T` *extends* `Pick`\<`Class`, `"id"` \| `"name"`\>

## Parameters

### courses

`Pick`\<[`Course`](../../types/course/type-aliases/Course.md), `"id"` \| `"name"` \| `"hiveClassId"`\>[]

Bluz courses.

### memberOf

`ReadonlySet`\<`number`\>

Hive group ids the user is a member of (`me.classes`).

### groups

`T`[]

Hive student groups the caller could list, for name matching.

## Returns

`string`[]

Ids of the user's courses, in course order.
