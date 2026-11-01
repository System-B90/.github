[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-access-tokens](../../../index.md) / [DbAccessTokens](../index.md) / authenticate

# Variable: authenticate

> `const` **authenticate**: (`token`) => `Promise`\<[`AccessTokenDocument`](../../../type-aliases/AccessTokenDocument.md) \| `null`\> = `authenticateToken`

Defined in: [ui/src/api-server/db-access-tokens.ts:179](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/db-access-tokens.ts#L179)

Resolve a presented token to its document, or null when it is malformed,
unknown, revoked or expired. Expiry is checked here rather than left to the
TTL index, which only sweeps on a ~60s cadence and keeps expired tokens
around for the UI on purpose.

## Parameters

### token

`string`

## Returns

`Promise`\<[`AccessTokenDocument`](../../../type-aliases/AccessTokenDocument.md) \| `null`\>
