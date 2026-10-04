[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / getSessionUser

# Function: getSessionUser()

> **getSessionUser**(): `Promise`\<[`SessionUser`](../type-aliases/SessionUser.md) \| `null`\>

Defined in: [ui/src/api-server/session-user.ts:18](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/session-user.ts#L18)

Resolves the currently authenticated user from the NextAuth session, or
`null` when there is no active session. Use for attributing server-side
writes (e.g. who last edited a shared draft).

## Returns

`Promise`\<[`SessionUser`](../type-aliases/SessionUser.md) \| `null`\>
