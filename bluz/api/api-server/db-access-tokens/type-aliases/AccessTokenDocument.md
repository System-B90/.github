[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-access-tokens](../index.md) / AccessTokenDocument

# Type Alias: AccessTokenDocument

> **AccessTokenDocument** = `object`

Defined in: [ui/src/api-server/db-access-tokens.ts:41](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-access-tokens.ts#L41)

One personal access token. `user` is the identity snapshot taken at
creation — the token acts as that user with that clearance, the same data a
next-auth session carries.

## Properties

### createdAt

> **createdAt**: `Date`

Defined in: [ui/src/api-server/db-access-tokens.ts:49](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-access-tokens.ts#L49)

***

### expiresAt

> **expiresAt**: `Date`

Defined in: [ui/src/api-server/db-access-tokens.ts:50](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-access-tokens.ts#L50)

***

### hint

> **hint**: `string`

Defined in: [ui/src/api-server/db-access-tokens.ts:48](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-access-tokens.ts#L48)

***

### id

> **id**: `string`

Defined in: [ui/src/api-server/db-access-tokens.ts:42](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-access-tokens.ts#L42)

***

### lastUsedAt

> **lastUsedAt**: `Date` \| `null`

Defined in: [ui/src/api-server/db-access-tokens.ts:51](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-access-tokens.ts#L51)

***

### name

> **name**: `string`

Defined in: [ui/src/api-server/db-access-tokens.ts:45](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-access-tokens.ts#L45)

***

### scope

> **scope**: [`AccessTokenScope`](../../../api-shared/types/access-token/enumerations/AccessTokenScope.md)

Defined in: [ui/src/api-server/db-access-tokens.ts:46](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-access-tokens.ts#L46)

***

### tokenHash

> **tokenHash**: `string`

Defined in: [ui/src/api-server/db-access-tokens.ts:47](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-access-tokens.ts#L47)

***

### user

> **user**: `AuthSessionUser`

Defined in: [ui/src/api-server/db-access-tokens.ts:44](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-access-tokens.ts#L44)

***

### userId

> **userId**: `string`

Defined in: [ui/src/api-server/db-access-tokens.ts:43](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-access-tokens.ts#L43)
