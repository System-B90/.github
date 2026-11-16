[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-access-tokens](../../../index.md) / [DbAccessTokens](../index.md) / revoke

# Variable: revoke

> `const` **revoke**: (`userId`, `id`) => `Promise`\<`void`\> = `revokeToken`

Defined in: [ui/src/api-server/db-access-tokens.ts:180](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/api-server/db-access-tokens.ts#L180)

Revoke one of the user's tokens. Scoped by `userId`, so nobody can revoke
someone else's token by guessing its id.

## Parameters

### userId

`string`

### id

`string`

## Returns

`Promise`\<`void`\>

## Throws

ClientApiError when the user has no token with that id.
