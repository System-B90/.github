[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-own-groups](../index.md) / getOwnHiveGroups

# Function: getOwnHiveGroups()

> **getOwnHiveGroups**(`userId`): `Promise`\<[`OwnHiveGroups`](../type-aliases/OwnHiveGroups.md) \| `null`\>

Defined in: [ui/src/api-server/student-own-groups.ts:60](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/student-own-groups.ts#L60)

The student's own Hive groups, for the board's default shuffle selection.
Never throws: no Hive session, Hive down, slow or refusing all yield null,
and the board falls back to showing everything the projection allows. No
Hive error detail is kept, logged to the response, or rethrown.

## Parameters

### userId

`string`

The session-derived user id — the cache key, never a request value.

## Returns

`Promise`\<[`OwnHiveGroups`](../type-aliases/OwnHiveGroups.md) \| `null`\>
