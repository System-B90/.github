[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / purgeGoogleEvents

# Function: purgeGoogleEvents()

> **purgeGoogleEvents**(`userId`, `scope`): `Promise`\<[`ApiGoogleCalendarPurgeResponse`](../../../../api-shared/types/google-calendar/type-aliases/ApiGoogleCalendarPurgeResponse.md)\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:1039](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/google/google-calendar-service.ts#L1039)

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
