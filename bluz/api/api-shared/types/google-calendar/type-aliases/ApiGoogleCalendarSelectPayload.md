[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/google-calendar](../index.md) / ApiGoogleCalendarSelectPayload

# Type Alias: ApiGoogleCalendarSelectPayload

> **ApiGoogleCalendarSelectPayload** = \{ `calendarId`: `string`; \} \| \{ `createNew`: `true`; \}

Defined in: [ui/src/api-shared/types/google-calendar.ts:111](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/google-calendar.ts#L111)

Re-point the link at another calendar. Exactly one of the two: an existing
(possibly shared) calendar by id, or a fresh Bluz-created one named after
the current iteration.
