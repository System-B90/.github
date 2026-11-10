[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / getStaffSession

# Function: getStaffSession()

> **getStaffSession**(): `Promise`\<`AuthSessionUser` & `object` \| `null`\>

Defined in: [ui/src/api-server/session-user.ts:189](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/session-user.ts#L189)

Non-throwing clearance check for *page* (RSC) code, where a throw becomes a
500 rather than a 403. Callers redirect on `false`. Route handlers must use
[requireStaffSession](requireStaffSession.md) instead. Pages are browser-only, so access
tokens are not consulted here.

## Returns

`Promise`\<`AuthSessionUser` & `object` \| `null`\>

The session user when they hold Segel/Admin clearance, else null.
