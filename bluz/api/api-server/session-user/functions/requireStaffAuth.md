[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / requireStaffAuth

# Function: requireStaffAuth()

> **requireStaffAuth**(): `Promise`\<[`RequestAuth`](../type-aliases/RequestAuth.md)\>

Defined in: [ui/src/api-server/session-user.ts:203](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/session-user.ts#L203)

Gates a route to Segel/Admin clearance (#199), returning how the caller
authenticated. Every request re-checks the JWT (or token), not just the
one-time sign-in gate in `sso.ts`'s `signInCallback`.

## Returns

`Promise`\<[`RequestAuth`](../type-aliases/RequestAuth.md)\>
