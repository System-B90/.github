[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-groups](../index.md) / EventHiveGroups

# Type Alias: EventHiveGroups\<T\>

> **EventHiveGroups**\<`T`\> = `object`

Defined in: [ui/src/api-shared/hive-groups.ts:28](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/hive-groups.ts#L28)

What an event's courses resolve to in Hive.

## Type Parameters

### T

`T`

## Properties

### groups

> **groups**: `T`[]

Defined in: [ui/src/api-shared/hive-groups.ts:30](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/hive-groups.ts#L30)

The groups the event reaches, deduplicated, in course order.

***

### unmatchedCourseIds

> **unmatchedCourseIds**: `string`[]

Defined in: [ui/src/api-shared/hive-groups.ts:32](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/hive-groups.ts#L32)

The event's own courses whose whole subtree matches no Hive group.
