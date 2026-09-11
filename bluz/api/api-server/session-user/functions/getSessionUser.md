[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / getSessionUser

# Function: getSessionUser()

> **getSessionUser**(): `Promise`\<[`SessionUser`](../type-aliases/SessionUser.md) \| `null`\>

Defined in: [ui/src/api-server/session-user.ts:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/session-user.ts#L18)

Resolves the currently authenticated user from the NextAuth session, or
`null` when there is no active session. Use for attributing server-side
writes (e.g. who last edited a shared draft).

## Returns

`Promise`\<[`SessionUser`](../type-aliases/SessionUser.md) \| `null`\>
