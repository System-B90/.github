[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-access-tokens](../../../index.md) / [DbAccessTokens](../index.md) / list

# Variable: list

> `const` **list**: (`userId`) => `Promise`\<[`AccessTokenSummary`](../../../../../api-shared/types/access-token/type-aliases/AccessTokenSummary.md)[]\> = `listTokens`

Defined in: [ui/src/api-server/db-access-tokens.ts:177](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/db-access-tokens.ts#L177)

The user's tokens, newest first. Expired ones stay listed until the TTL sweep.

## Parameters

### userId

`string`

## Returns

`Promise`\<[`AccessTokenSummary`](../../../../../api-shared/types/access-token/type-aliases/AccessTokenSummary.md)[]\>
