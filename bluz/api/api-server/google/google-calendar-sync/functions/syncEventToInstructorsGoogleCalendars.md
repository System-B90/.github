[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-sync](../index.md) / syncEventToInstructorsGoogleCalendars

# Function: syncEventToInstructorsGoogleCalendars()

> **syncEventToInstructorsGoogleCalendars**(`event`, `action`, `iterationId?`, `previous?`): `void`

Defined in: [ui/src/api-server/google/google-calendar-sync.ts:99](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/google/google-calendar-sync.ts#L99)

Fire-and-forget: mirrors the given event into every linked Google calendar
that wants it — one write per calendar, however many users share it. A
calendar wants the event when any of its users is an assigned instructor
or lecturer, or opted into syncing every event. When `previous` is given
(an update), calendars that wanted the old version but not the new one
(say, the instructor was swapped) get a delete, so nothing is orphaned.
Never throws — a Google outage or missing configuration must never affect
the Bluz event write it's attached to.

## Parameters

### event

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

### action

`"upsert"` \| `"delete"`

### iterationId?

`string`

### previous?

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

## Returns

`void`
