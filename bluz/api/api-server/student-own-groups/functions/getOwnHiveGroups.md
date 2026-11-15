[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-own-groups](../index.md) / getOwnHiveGroups

# Function: getOwnHiveGroups()

> **getOwnHiveGroups**(`userId`): `Promise`\<[`OwnHiveGroups`](../type-aliases/OwnHiveGroups.md) \| `null`\>

Defined in: [ui/src/api-server/student-own-groups.ts:60](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/student-own-groups.ts#L60)

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
