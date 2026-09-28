[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/google-calendar](../index.md) / ApiGoogleCalendarSelectPayload

# Type Alias: ApiGoogleCalendarSelectPayload

> **ApiGoogleCalendarSelectPayload** = \{ `calendarId`: `string`; \} \| \{ `createNew`: `true`; \}

Defined in: [ui/src/api-shared/types/google-calendar.ts:103](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/types/google-calendar.ts#L103)

Re-point the link at another calendar. Exactly one of the two: an existing
(possibly shared) calendar by id, or a fresh Bluz-created one named after
the current iteration.
