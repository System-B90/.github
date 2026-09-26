[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / selectGoogleCalendar

# Function: selectGoogleCalendar()

> **selectGoogleCalendar**(`userId`, `payload`): `Promise`\<[`GoogleCalendarSelection`](../../../../api-shared/types/google-calendar/type-aliases/GoogleCalendarSelection.md)\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:555](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/google/google-calendar-service.ts#L555)

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
