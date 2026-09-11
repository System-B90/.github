[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/calendar/snapshots/restore/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/snapshots/restore/route.ts:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/api/calendar/snapshots/restore/route.ts#L17)

POST /api/calendar/snapshots/restore?id=<uuid>

Restores the calendar to the snapshot's captured state within the snapshot's
own date range: live events in that range are archived, the snapshot's
events are written back, and all connected clients are notified via
WebSocket broadcasts.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
