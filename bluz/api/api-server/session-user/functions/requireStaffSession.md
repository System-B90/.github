[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / requireStaffSession

# Function: requireStaffSession()

> **requireStaffSession**(): `Promise`\<`AuthSessionUser` & `object`\>

Defined in: [ui/src/api-server/session-user.ts:58](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/session-user.ts#L58)

Gates a route to Segel/Admin clearance (#199). Every request re-checks the
JWT, not just the one-time sign-in gate in `sso.ts`'s `signInCallback`.
Throws so callers can just `await requireStaffSession()` at the top of a
`withApi` handler and let `catchHandler` map it to 401/403.

## Returns

`Promise`\<`AuthSessionUser` & `object`\>
