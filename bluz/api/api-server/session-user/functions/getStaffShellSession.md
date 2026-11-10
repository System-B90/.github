[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / getStaffShellSession

# Function: getStaffShellSession()

> **getStaffShellSession**(): `Promise`\<`AuthSessionUser` & `object` \| `null`\>

Defined in: [ui/src/api-server/session-user.ts:209](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/session-user.ts#L209)

Like [getStaffSession](getStaffSession.md), but also admits a Checker — for page code and
read-only handlers that serve the staff shell rather than gate a write.

## Returns

`Promise`\<`AuthSessionUser` & `object` \| `null`\>

The session user when they may enter the staff shell, else null.
