[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/use-hive-student-groups](../index.md) / findShuffleHiveGroup

# Function: findShuffleHiveGroup()

> **findShuffleHiveGroup**(`groups`, `name`, `linkedGroupId?`): `Class` \| `undefined`

Defined in: [ui/src/components/gantt/use-hive-student-groups.ts:57](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/use-hive-student-groups.ts#L57)

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
