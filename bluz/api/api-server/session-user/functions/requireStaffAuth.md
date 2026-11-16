[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / requireStaffAuth

# Function: requireStaffAuth()

> **requireStaffAuth**(): `Promise`\<[`RequestAuth`](../type-aliases/RequestAuth.md)\>

Defined in: [ui/src/api-server/session-user.ts:229](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/session-user.ts#L229)

Gates a route to Segel/Admin clearance (#199), returning how the caller
authenticated. Every request re-checks the JWT (or token), not just the
one-time sign-in gate in `sso.ts`'s `signInCallback`.

A Checker passes too, but only for a read (GET/HEAD) outside
`CHECKER_DENIED_API_PREFIXES` — see `api-shared/clearance.ts`. The check is
on the user's clearance, so it holds for an access token a Checker holds.

## Returns

`Promise`\<[`RequestAuth`](../type-aliases/RequestAuth.md)\>
