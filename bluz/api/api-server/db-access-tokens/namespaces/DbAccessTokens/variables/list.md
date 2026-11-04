[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-access-tokens](../../../index.md) / [DbAccessTokens](../index.md) / list

# Variable: list

> `const` **list**: (`userId`) => `Promise`\<[`AccessTokenSummary`](../../../../../api-shared/types/access-token/type-aliases/AccessTokenSummary.md)[]\> = `listTokens`

Defined in: [ui/src/api-server/db-access-tokens.ts:177](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/db-access-tokens.ts#L177)

The user's tokens, newest first. Expired ones stay listed until the TTL sweep.

## Parameters

### userId

`string`

## Returns

`Promise`\<[`AccessTokenSummary`](../../../../../api-shared/types/access-token/type-aliases/AccessTokenSummary.md)[]\>
