[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / listGoogleCalendarOptions

# Function: listGoogleCalendarOptions()

> **listGoogleCalendarOptions**(`userId`): `Promise`\<\{ `calendars`: [`GoogleCalendarOption`](../../../../api-shared/types/google-calendar/type-aliases/GoogleCalendarOption.md)[]; `selectedId`: `string`; \}\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:540](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/google/google-calendar-service.ts#L540)

Calendars the connected user could mirror into — their own plus any a
colleague shared with write access. Throws when not connected.

## Parameters

### userId

`string`

## Returns

`Promise`\<\{ `calendars`: [`GoogleCalendarOption`](../../../../api-shared/types/google-calendar/type-aliases/GoogleCalendarOption.md)[]; `selectedId`: `string`; \}\>
