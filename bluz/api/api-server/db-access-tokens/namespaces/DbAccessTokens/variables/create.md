[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-access-tokens](../../../index.md) / [DbAccessTokens](../index.md) / create

# Variable: create

> `const` **create**: (`user`, `name`, `scope`, `expiresInDays`) => `Promise`\<[`ApiAccessTokenCreateResponse`](../../../../../api-shared/types/access-token/type-aliases/ApiAccessTokenCreateResponse.md)\> = `createToken`

Defined in: [ui/src/api-server/db-access-tokens.ts:178](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/db-access-tokens.ts#L178)

Mint a token for `user`.

## Parameters

### user

`AuthSessionUser`

### name

`string`

### scope

[`AccessTokenScope`](../../../../../api-shared/types/access-token/enumerations/AccessTokenScope.md)

### expiresInDays

`7` \| `30` \| `90` \| `180` \| `365`

## Returns

`Promise`\<[`ApiAccessTokenCreateResponse`](../../../../../api-shared/types/access-token/type-aliases/ApiAccessTokenCreateResponse.md)\>

## Throws

ClientApiError on a blank/too-long name or when the user already
        holds [ACCESS\_TOKEN\_MAX\_PER\_USER](../../../../../api-shared/types/access-token/variables/ACCESS_TOKEN_MAX_PER_USER.md) live tokens.
