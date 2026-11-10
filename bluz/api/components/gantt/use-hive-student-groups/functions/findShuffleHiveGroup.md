[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/use-hive-student-groups](../index.md) / findShuffleHiveGroup

# Function: findShuffleHiveGroup()

> **findShuffleHiveGroup**(`groups`, `name`, `linkedGroupId?`): `Class` \| `undefined`

Defined in: [ui/src/components/gantt/use-hive-student-groups.ts:55](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/use-hive-student-groups.ts#L55)

The Hive group a shuffle syncs against: its explicitly linked group when
the syllabus sets one (#774), else the same-named group.

## Parameters

### groups

`HiveStudentGroups` \| `null`

### name

`string`

### linkedGroupId?

`number`

## Returns

`Class` \| `undefined`
