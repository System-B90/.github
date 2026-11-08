[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-groups](../index.md) / EventHiveGroups

# Type Alias: EventHiveGroups\<T\>

> **EventHiveGroups**\<`T`\> = `object`

Defined in: [ui/src/api-shared/hive-groups.ts:28](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/hive-groups.ts#L28)

What an event's courses resolve to in Hive.

## Type Parameters

### T

`T`

## Properties

### groups

> **groups**: `T`[]

Defined in: [ui/src/api-shared/hive-groups.ts:30](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/hive-groups.ts#L30)

The groups the event reaches, deduplicated, in course order.

***

### unmatchedCourseIds

> **unmatchedCourseIds**: `string`[]

Defined in: [ui/src/api-shared/hive-groups.ts:32](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/hive-groups.ts#L32)

The event's own courses whose whole subtree matches no Hive group.
