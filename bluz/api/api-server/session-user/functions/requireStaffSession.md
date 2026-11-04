[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / requireStaffSession

# Function: requireStaffSession()

> **requireStaffSession**(): `Promise`\<`AuthSessionUser` & `object`\>

Defined in: [ui/src/api-server/session-user.ts:233](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/session-user.ts#L233)

Gates a route to Segel/Admin clearance (#199). Accepts a browser session or
a personal access token. Throws so callers can just
`await requireStaffSession()` at the top of a `withApi` handler and let
`catchHandler` map it to 401/403.

## Returns

`Promise`\<`AuthSessionUser` & `object`\>
