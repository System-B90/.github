[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / connectGoogleCalendar

# Function: connectGoogleCalendar()

> **connectGoogleCalendar**(`userId`, `code`): `Promise`\<`void`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:503](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/google/google-calendar-service.ts#L503)

Exchanges the GIS popup authorization `code` for tokens, finds (or creates)
the calendar for the current iteration in the user's account, and persists
the link. The popup code model requires the reserved `"postmessage"`
redirect_uri during token exchange — passing the page origin fails with
invalid_request.

## Parameters

### userId

`string`

### code

`string`

## Returns

`Promise`\<`void`\>
