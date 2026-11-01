[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / listGoogleCalendarOptions

# Function: listGoogleCalendarOptions()

> **listGoogleCalendarOptions**(`userId`): `Promise`\<\{ `calendars`: [`GoogleCalendarOption`](../../../../api-shared/types/google-calendar/type-aliases/GoogleCalendarOption.md)[]; `selectedId`: `string`; \}\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:658](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/google/google-calendar-service.ts#L658)

Calendars the connected user could mirror into — their own plus any a
colleague shared with write access. Throws when not connected.

## Parameters

### userId

`string`

## Returns

`Promise`\<\{ `calendars`: [`GoogleCalendarOption`](../../../../api-shared/types/google-calendar/type-aliases/GoogleCalendarOption.md)[]; `selectedId`: `string`; \}\>
