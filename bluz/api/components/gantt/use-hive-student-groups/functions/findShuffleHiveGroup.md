[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/use-hive-student-groups](../index.md) / findShuffleHiveGroup

# Function: findShuffleHiveGroup()

> **findShuffleHiveGroup**(`groups`, `name`, `linkedGroupId?`): `Class` \| `undefined`

Defined in: [ui/src/components/gantt/use-hive-student-groups.ts:57](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/gantt/use-hive-student-groups.ts#L57)

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
