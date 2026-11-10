[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/hive-groups](../index.md) / EventHiveGroups

# Type Alias: EventHiveGroups\<T\>

> **EventHiveGroups**\<`T`\> = `object`

Defined in: [ui/src/api-shared/hive-groups.ts:56](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/hive-groups.ts#L56)

What an event's courses resolve to in Hive.

## Type Parameters

### T

`T`

## Properties

### groups

> **groups**: `T`[]

Defined in: [ui/src/api-shared/hive-groups.ts:58](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/hive-groups.ts#L58)

The groups the event reaches, deduplicated, in course order.

***

### unmatchedCourseIds

> **unmatchedCourseIds**: `string`[]

Defined in: [ui/src/api-shared/hive-groups.ts:60](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/hive-groups.ts#L60)

The event's own courses whose whole subtree matches no Hive group.
