[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/use-hive-student-groups](../index.md) / useHiveStudentGroups

# Function: useHiveStudentGroups()

> **useHiveStudentGroups**(): `HiveStudentGroups` \| `null`

Defined in: [ui/src/components/gantt/use-hive-student-groups.ts:25](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/use-hive-student-groups.ts#L25)

Hive student groups, keyed by normalized name. A shuffle is 1:1 with a Hive
student group matched by name (see `resolveDesiredRules`), so this tells a
shuffle whether it is linked and what its Hive description is. `null` while
loading or when Hive is unreachable: callers must still work offline.

## Returns

`HiveStudentGroups` \| `null`
