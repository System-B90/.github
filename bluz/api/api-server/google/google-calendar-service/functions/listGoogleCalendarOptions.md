[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / listGoogleCalendarOptions

# Function: listGoogleCalendarOptions()

> **listGoogleCalendarOptions**(`userId`): `Promise`\<\{ `calendars`: [`GoogleCalendarOption`](../../../../api-shared/types/google-calendar/type-aliases/GoogleCalendarOption.md)[]; `selectedId`: `string`; \}\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:658](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/google/google-calendar-service.ts#L658)

Calendars the connected user could mirror into — their own plus any a
colleague shared with write access. Throws when not connected.

## Parameters

### userId

`string`

## Returns

`Promise`\<\{ `calendars`: [`GoogleCalendarOption`](../../../../api-shared/types/google-calendar/type-aliases/GoogleCalendarOption.md)[]; `selectedId`: `string`; \}\>
