[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / purgeGoogleEvents

# Function: purgeGoogleEvents()

> **purgeGoogleEvents**(`userId`, `scope`): `Promise`\<[`ApiGoogleCalendarPurgeResponse`](../../../../api-shared/types/google-calendar/type-aliases/ApiGoogleCalendarPurgeResponse.md)\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:1164](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/google/google-calendar-service.ts#L1164)

Removes Bluz-tagged events from the user's linked Google calendar — the
orphaned ones, or all of them. Never touches events created by hand in
Google. Deletes run sequentially with backoff; one that still fails is
counted, not thrown, so the rest of the purge completes.

## Parameters

### userId

`string`

### scope

[`GoogleCalendarPurgeScope`](../../../../api-shared/types/google-calendar/type-aliases/GoogleCalendarPurgeScope.md)

## Returns

`Promise`\<[`ApiGoogleCalendarPurgeResponse`](../../../../api-shared/types/google-calendar/type-aliases/ApiGoogleCalendarPurgeResponse.md)\>
