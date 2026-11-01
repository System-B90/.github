[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-groups](../index.md) / resolveEventHiveGroups

# Function: resolveEventHiveGroups()

> **resolveEventHiveGroups**\<`T`\>(`courseIds`, `resolveDescendants`, `courseById`, `groups`): [`EventHiveGroups`](../type-aliases/EventHiveGroups.md)\<`T`\>

Defined in: [ui/src/api-shared/hive-groups.ts:48](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/hive-groups.ts#L48)

The Hive student groups an event reaches: those of its courses and of all
their sub-courses, since groups exist per shuffle and an event set on a
parent course (Bis90, Apollo) would otherwise reach nobody (#974). The ICS
feed, the go-live activator and the schedule's lesson check all agree on
this one rule.

## Type Parameters

### T

`T` *extends* `Pick`\<`Class`, `"id"` \| `"name"`\>

## Parameters

### courseIds

`string`[]

The event's courses.

### resolveDescendants

(`courseIds`) => `Set`\<`string`\>

`descendantCoursesResolver` over the course list.

### courseById

`Map`\<`string`, `Pick`\<[`Course`](../../types/course/type-aliases/Course.md), `"name"` \| `"hiveClassId"`\>\>

Bluz course id → course.

### groups

`T`[]

Hive student groups.

## Returns

[`EventHiveGroups`](../type-aliases/EventHiveGroups.md)\<`T`\>

The groups reached, and the courses that reach none.
