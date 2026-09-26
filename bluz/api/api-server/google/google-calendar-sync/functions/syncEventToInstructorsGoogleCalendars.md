[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-sync](../index.md) / syncEventToInstructorsGoogleCalendars

# Function: syncEventToInstructorsGoogleCalendars()

> **syncEventToInstructorsGoogleCalendars**(`event`, `action`, `iterationId?`, `previous?`): `void`

Defined in: [ui/src/api-server/google/google-calendar-sync.ts:93](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/google/google-calendar-sync.ts#L93)

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

`"delete"` \| `"upsert"`

### iterationId?

`string`

### previous?

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

## Returns

`void`
