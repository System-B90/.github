[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / requireStaffSession

# Function: requireStaffSession()

> **requireStaffSession**(): `Promise`\<`AuthSessionUser` & `object`\>

Defined in: [ui/src/api-server/session-user.ts:264](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/session-user.ts#L264)

Gates a route to Segel/Admin clearance (#199). Accepts a browser session or
a personal access token. Throws so callers can just
`await requireStaffSession()` at the top of a `withApi` handler and let
`catchHandler` map it to 401/403.

## Returns

`Promise`\<`AuthSessionUser` & `object`\>
