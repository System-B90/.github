[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / purgeGoogleEvents

# Function: purgeGoogleEvents()

> **purgeGoogleEvents**(`userId`, `scope`): `Promise`\<[`ApiGoogleCalendarPurgeResponse`](../../../../api-shared/types/google-calendar/type-aliases/ApiGoogleCalendarPurgeResponse.md)\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:1039](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/google/google-calendar-service.ts#L1039)

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
