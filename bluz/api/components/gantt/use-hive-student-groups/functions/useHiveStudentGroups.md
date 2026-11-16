[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/use-hive-student-groups](../index.md) / useHiveStudentGroups

# Function: useHiveStudentGroups()

> **useHiveStudentGroups**(): `HiveStudentGroups` \| `null`

Defined in: [ui/src/components/gantt/use-hive-student-groups.ts:26](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/gantt/use-hive-student-groups.ts#L26)

Hive student groups, keyed by normalized name. A shuffle is 1:1 with a Hive
student group matched by name (see `findCourseHiveGroup`), so this tells a
shuffle whether it is linked and what its Hive description is. `null` while
loading or when Hive is unreachable: callers must still work offline.

## Returns

`HiveStudentGroups` \| `null`
