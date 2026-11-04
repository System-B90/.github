[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/access-token](../index.md) / ApiAccessTokenCurrentResponse

# Type Alias: ApiAccessTokenCurrentResponse

> **ApiAccessTokenCurrentResponse** = `object`

Defined in: [ui/src/api-shared/types/access-token.ts:72](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/access-token.ts#L72)

`GET /api/access-tokens/current`: who the calling token acts as. Shaped
like next-auth's `/api/auth/session` so `bz.whoami()` parses either.

## Properties

### accessToken

> **accessToken**: [`AccessTokenSummary`](AccessTokenSummary.md)

Defined in: [ui/src/api-shared/types/access-token.ts:75](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/access-token.ts#L75)

***

### expires

> **expires**: `string`

Defined in: [ui/src/api-shared/types/access-token.ts:74](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/access-token.ts#L74)

***

### user

> **user**: `object`

Defined in: [ui/src/api-shared/types/access-token.ts:73](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/access-token.ts#L73)

#### email

> **email**: `null` \| `string`

#### id

> **id**: `string`

#### name

> **name**: `string`
