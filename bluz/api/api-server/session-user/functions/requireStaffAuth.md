[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / requireStaffAuth

# Function: requireStaffAuth()

> **requireStaffAuth**(): `Promise`\<[`RequestAuth`](../type-aliases/RequestAuth.md)\>

Defined in: [ui/src/api-server/session-user.ts:203](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/session-user.ts#L203)

Gates a route to Segel/Admin clearance (#199), returning how the caller
authenticated. Every request re-checks the JWT (or token), not just the
one-time sign-in gate in `sso.ts`'s `signInCallback`.

## Returns

`Promise`\<[`RequestAuth`](../type-aliases/RequestAuth.md)\>
