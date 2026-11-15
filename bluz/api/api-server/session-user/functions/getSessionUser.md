[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / getSessionUser

# Function: getSessionUser()

> **getSessionUser**(): `Promise`\<[`SessionUser`](../type-aliases/SessionUser.md) \| `null`\>

Defined in: [ui/src/api-server/session-user.ts:168](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/api-server/session-user.ts#L168)

Resolves the currently authenticated user from the NextAuth session (or a
personal access token), or `null` when there is none. Use for attributing
server-side writes (e.g. who last edited a shared draft).

## Returns

`Promise`\<[`SessionUser`](../type-aliases/SessionUser.md) \| `null`\>
