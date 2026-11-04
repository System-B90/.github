[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/google-calendar](../index.md) / ApiGoogleCalendarSelectPayload

# Type Alias: ApiGoogleCalendarSelectPayload

> **ApiGoogleCalendarSelectPayload** = \{ `calendarId`: `string`; \} \| \{ `createNew`: `true`; \}

Defined in: [ui/src/api-shared/types/google-calendar.ts:111](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/types/google-calendar.ts#L111)

Re-point the link at another calendar. Exactly one of the two: an existing
(possibly shared) calendar by id, or a fresh Bluz-created one named after
the current iteration.
