[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / requireStaffSession

# Function: requireStaffSession()

> **requireStaffSession**(): `Promise`\<`AuthSessionUser` & `object`\>

Defined in: [ui/src/api-server/session-user.ts:233](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/session-user.ts#L233)

Gates a route to Segel/Admin clearance (#199). Accepts a browser session or
a personal access token. Throws so callers can just
`await requireStaffSession()` at the top of a `withApi` handler and let
`catchHandler` map it to 401/403.

## Returns

`Promise`\<`AuthSessionUser` & `object`\>
