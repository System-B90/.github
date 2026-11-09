[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / getSessionUser

# Function: getSessionUser()

> **getSessionUser**(): `Promise`\<[`SessionUser`](../type-aliases/SessionUser.md) \| `null`\>

Defined in: [ui/src/api-server/session-user.ts:168](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/session-user.ts#L168)

Resolves the currently authenticated user from the NextAuth session (or a
personal access token), or `null` when there is none. Use for attributing
server-side writes (e.g. who last edited a shared draft).

## Returns

`Promise`\<[`SessionUser`](../type-aliases/SessionUser.md) \| `null`\>
