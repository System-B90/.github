[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / RequestAuth

# Type Alias: RequestAuth

> **RequestAuth** = `object`

Defined in: [ui/src/api-server/session-user.ts:31](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/session-user.ts#L31)

Who is calling, and how. `accessToken` is set when the caller sent a
personal access token instead of a browser session cookie.

## Properties

### accessToken

> **accessToken**: [`AccessTokenDocument`](../../db-access-tokens/type-aliases/AccessTokenDocument.md) \| `null`

Defined in: [ui/src/api-server/session-user.ts:33](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/session-user.ts#L33)

***

### user

> **user**: `AuthSessionUser`

Defined in: [ui/src/api-server/session-user.ts:32](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/session-user.ts#L32)
