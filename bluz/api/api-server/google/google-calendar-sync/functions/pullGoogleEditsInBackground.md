[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-sync](../index.md) / pullGoogleEditsInBackground

# Function: pullGoogleEditsInBackground()

> **pullGoogleEditsInBackground**(`userId`): `void`

Defined in: [ui/src/api-server/google/google-calendar-sync.ts:155](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/google/google-calendar-sync.ts#L155)

Fire-and-forget, throttled (per user, 5 min): pulls Google-side edits of
Bluz-pushed events back into Bluz. Hung off calendar reads so Google edits
flow in while users browse, without polling infrastructure. Updates land
via DbEvent.set, which broadcasts over WebSocket to open clients.

## Parameters

### userId

`string`

## Returns

`void`
