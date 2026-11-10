[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-own-groups](../index.md) / OwnHiveGroups

# Type Alias: OwnHiveGroups

> **OwnHiveGroups** = `object`

Defined in: [ui/src/api-server/student-own-groups.ts:5](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/student-own-groups.ts#L5)

A student's own Hive student groups, as their own Hive login sees them.

## Properties

### groups

> **groups**: `Pick`\<`Class`, `"id"` \| `"name"`\>[]

Defined in: [ui/src/api-server/student-own-groups.ts:12](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/student-own-groups.ts#L12)

Student groups the student's token could list, for name matching. Empty
when Hive refuses a Hanich the listing: explicit links still resolve.

***

### memberOf

> **memberOf**: `ReadonlySet`\<`number`\>

Defined in: [ui/src/api-server/student-own-groups.ts:7](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/student-own-groups.ts#L7)

Hive group ids the student is a member of (`me.classes`).
