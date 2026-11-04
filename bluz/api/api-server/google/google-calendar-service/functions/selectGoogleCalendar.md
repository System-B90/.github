[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / selectGoogleCalendar

# Function: selectGoogleCalendar()

> **selectGoogleCalendar**(`userId`, `payload`): `Promise`\<[`GoogleCalendarSelection`](../../../../api-shared/types/google-calendar/type-aliases/GoogleCalendarSelection.md)\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:676](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/google/google-calendar-service.ts#L676)

Re-points the user's link at another calendar (an existing writable one,
typically shared by a colleague, or a fresh Bluz-created one). The sync
cursor is dropped — it belonged to the previous calendar — and the link's
iteration is reset to the current one, which is what the new calendar will
mirror from now on.

## Parameters

### userId

`string`

### payload

[`ApiGoogleCalendarSelectPayload`](../../../../api-shared/types/google-calendar/type-aliases/ApiGoogleCalendarSelectPayload.md)

## Returns

`Promise`\<[`GoogleCalendarSelection`](../../../../api-shared/types/google-calendar/type-aliases/GoogleCalendarSelection.md)\>
