[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-service](../index.md) / pullEventEdits

# Function: pullEventEdits()

> **pullEventEdits**(`userId`): `Promise`\<`number`\>

Defined in: [ui/src/api-server/google/google-calendar-service.ts:762](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/google/google-calendar-service.ts#L762)

Pulls Google-side edits from the user's linked calendar back into Bluz
using the Calendar API incremental-sync protocol: the first call does a
full list and stores `nextSyncToken`; later calls send that token and
receive only what changed since. A 410 GONE (expired token) clears the
cursor and retries with a full resync, per Google's docs.
Returns the number of Bluz events updated; 0 (never throws) on any failure.

## Parameters

### userId

`string`

## Returns

`Promise`\<`number`\>
