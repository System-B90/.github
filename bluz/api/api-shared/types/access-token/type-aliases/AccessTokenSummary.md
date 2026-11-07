[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/access-token](../index.md) / AccessTokenSummary

# Type Alias: AccessTokenSummary

> **AccessTokenSummary** = `object`

Defined in: [ui/src/api-shared/types/access-token.ts:42](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/access-token.ts#L42)

What the API shows about a token. The secret itself is never returned after creation.

## Properties

### createdAt

> **createdAt**: `string`

Defined in: [ui/src/api-shared/types/access-token.ts:49](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/access-token.ts#L49)

ISO timestamps.

***

### expiresAt

> **expiresAt**: `string`

Defined in: [ui/src/api-shared/types/access-token.ts:50](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/access-token.ts#L50)

***

### hint

> **hint**: `string`

Defined in: [ui/src/api-shared/types/access-token.ts:47](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/access-token.ts#L47)

Last 4 characters of the secret, to tell tokens apart.

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types/access-token.ts:43](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/access-token.ts#L43)

***

### lastUsedAt

> **lastUsedAt**: `null` \| `string`

Defined in: [ui/src/api-shared/types/access-token.ts:51](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/access-token.ts#L51)

***

### name

> **name**: `string`

Defined in: [ui/src/api-shared/types/access-token.ts:44](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/access-token.ts#L44)

***

### scope

> **scope**: [`AccessTokenScope`](../enumerations/AccessTokenScope.md)

Defined in: [ui/src/api-shared/types/access-token.ts:45](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/access-token.ts#L45)
