[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/google/google-calendar-sync](../index.md) / pullGoogleEditsInBackground

# Function: pullGoogleEditsInBackground()

> **pullGoogleEditsInBackground**(`userId`): `void`

Defined in: [ui/src/api-server/google/google-calendar-sync.ts:155](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/google/google-calendar-sync.ts#L155)

Fire-and-forget, throttled (per user, 5 min): pulls Google-side edits of
Bluz-pushed events back into Bluz. Hung off calendar reads so Google edits
flow in while users browse, without polling infrastructure. Updates land
via DbEvent.set, which broadcasts over WebSocket to open clients.

## Parameters

### userId

`string`

## Returns

`void`
