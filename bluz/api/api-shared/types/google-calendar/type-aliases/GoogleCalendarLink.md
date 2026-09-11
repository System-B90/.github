[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/google-calendar](../index.md) / GoogleCalendarLink

# Type Alias: GoogleCalendarLink

> **GoogleCalendarLink** = `object`

Defined in: [ui/src/api-shared/types/google-calendar.ts:5](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/google-calendar.ts#L5)

Per-user OAuth link to Google Calendar. Stored server-side only — never sent
to the client as-is (see [GoogleCalendarStatus](GoogleCalendarStatus.md)).

## Properties

### accessToken

> **accessToken**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:8](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/google-calendar.ts#L8)

AES-GCM sealed (see api-server/secret-box.ts) — never stored in plaintext.

***

### calendarId

> **calendarId**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:14](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/google-calendar.ts#L14)

Dedicated calendar Bluz created in the user's Google account to mirror their events.

***

### connectedAt

> **connectedAt**: `number`

Defined in: [ui/src/api-shared/types/google-calendar.ts:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/google-calendar.ts#L17)

***

### expiryDate

> **expiryDate**: `number`

Defined in: [ui/src/api-shared/types/google-calendar.ts:12](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/google-calendar.ts#L12)

Epoch ms when `accessToken` expires.

***

### refreshToken

> **refreshToken**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:10](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/google-calendar.ts#L10)

AES-GCM sealed (see api-server/secret-box.ts) — never stored in plaintext.

***

### syncToken?

> `optional` **syncToken?**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/google-calendar.ts#L16)

Incremental sync cursor for pulling changes back from Google (nextSyncToken).

***

### userId

> **userId**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:6](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/google-calendar.ts#L6)
