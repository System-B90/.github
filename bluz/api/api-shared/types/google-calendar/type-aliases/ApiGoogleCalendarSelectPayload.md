[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/google-calendar](../index.md) / ApiGoogleCalendarSelectPayload

# Type Alias: ApiGoogleCalendarSelectPayload

> **ApiGoogleCalendarSelectPayload** = \{ `calendarId`: `string`; \} \| \{ `createNew`: `true`; \}

Defined in: [ui/src/api-shared/types/google-calendar.ts:111](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types/google-calendar.ts#L111)

Re-point the link at another calendar. Exactly one of the two: an existing
(possibly shared) calendar by id, or a fresh Bluz-created one named after
the current iteration.
