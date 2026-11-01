[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / requireStaffSession

# Function: requireStaffSession()

> **requireStaffSession**(): `Promise`\<`AuthSessionUser` & `object`\>

Defined in: [ui/src/api-server/session-user.ts:233](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/session-user.ts#L233)

Gates a route to Segel/Admin clearance (#199). Accepts a browser session or
a personal access token. Throws so callers can just
`await requireStaffSession()` at the top of a `withApi` handler and let
`catchHandler` map it to 401/403.

## Returns

`Promise`\<`AuthSessionUser` & `object`\>
