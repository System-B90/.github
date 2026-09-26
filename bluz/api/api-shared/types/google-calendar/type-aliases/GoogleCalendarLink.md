[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/google-calendar](../index.md) / GoogleCalendarLink

# Type Alias: GoogleCalendarLink

> **GoogleCalendarLink** = `object`

Defined in: [ui/src/api-shared/types/google-calendar.ts:12](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L12)

Per-user OAuth link to Google Calendar. Stored server-side only — never sent
to the client as-is (see [GoogleCalendarStatus](GoogleCalendarStatus.md)).

Several users may point their links at the *same* Google calendar (one
shared by its owner with the rest of the staff). The sync fan-out groups
links by `calendarId` so a shared calendar receives each event once, and
the link's `iterationId` pins which Bluz iteration that calendar mirrors.

## Properties

### accessToken

> **accessToken**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:15](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L15)

AES-GCM sealed (see api-server/secret-box.ts) — never stored in plaintext.

***

### calendarAccessRole?

> `optional` **calendarAccessRole?**: [`GoogleCalendarAccessRole`](GoogleCalendarAccessRole.md)

Defined in: [ui/src/api-shared/types/google-calendar.ts:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L25)

The user's Calendar API access role on it (`owner` / `writer`).

***

### calendarId

> **calendarId**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:21](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L21)

Google calendar this link mirrors into — Bluz-created, or one shared with the user.

***

### calendarSummary?

> `optional` **calendarSummary?**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:23](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L23)

Display name of that calendar at link time (cosmetic; Google is the source of truth).

***

### connectedAt

> **connectedAt**: `number`

Defined in: [ui/src/api-shared/types/google-calendar.ts:35](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L35)

***

### expiryDate

> **expiryDate**: `number`

Defined in: [ui/src/api-shared/types/google-calendar.ts:19](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L19)

Epoch ms when `accessToken` expires.

***

### iterationId?

> `optional` **iterationId?**: [`IterationId`](../../iteration/type-aliases/IterationId.md)

Defined in: [ui/src/api-shared/types/google-calendar.ts:32](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L32)

Bluz iteration this calendar mirrors. Events of any other iteration are
never pushed here, and a pulled-back edit resolves against this one.
Links made before this field existed have none and fall back to the
current iteration.

***

### refreshToken

> **refreshToken**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:17](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L17)

AES-GCM sealed (see api-server/secret-box.ts) — never stored in plaintext.

***

### syncToken?

> `optional` **syncToken?**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:34](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L34)

Incremental sync cursor for pulling changes back from Google (nextSyncToken).

***

### userId

> **userId**: `string`

Defined in: [ui/src/api-shared/types/google-calendar.ts:13](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/google-calendar.ts#L13)
