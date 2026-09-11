[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / getStaffSession

# Function: getStaffSession()

> **getStaffSession**(): `Promise`\<`AuthSessionUser` & `object` \| `null`\>

Defined in: [ui/src/api-server/session-user.ts:38](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/session-user.ts#L38)

Non-throwing clearance check for *page* (RSC) code, where a throw becomes a
500 rather than a 403. Callers redirect on `false`. Route handlers must use
[requireStaffSession](requireStaffSession.md) instead.

## Returns

`Promise`\<`AuthSessionUser` & `object` \| `null`\>

The session user when they hold Segel/Admin clearance, else null.
