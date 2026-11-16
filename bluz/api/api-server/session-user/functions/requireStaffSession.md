[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/session-user](../index.md) / requireStaffSession

# Function: requireStaffSession()

> **requireStaffSession**(): `Promise`\<`AuthSessionUser` & `object`\>

Defined in: [ui/src/api-server/session-user.ts:264](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/session-user.ts#L264)

Gates a route to Segel/Admin clearance (#199). Accepts a browser session or
a personal access token. Throws so callers can just
`await requireStaffSession()` at the top of a `withApi` handler and let
`catchHandler` map it to 401/403.

## Returns

`Promise`\<`AuthSessionUser` & `object`\>
