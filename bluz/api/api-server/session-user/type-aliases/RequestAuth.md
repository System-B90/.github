[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / RequestAuth

# Type Alias: RequestAuth

> **RequestAuth** = `object`

Defined in: [ui/src/api-server/session-user.ts:37](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/session-user.ts#L37)

Who is calling, and how. `accessToken` is set when the caller sent a
personal access token instead of a browser session cookie.

## Properties

### accessToken

> **accessToken**: [`AccessTokenDocument`](../../db-access-tokens/type-aliases/AccessTokenDocument.md) \| `null`

Defined in: [ui/src/api-server/session-user.ts:39](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/session-user.ts#L39)

***

### user

> **user**: `AuthSessionUser`

Defined in: [ui/src/api-server/session-user.ts:38](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/session-user.ts#L38)
