[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/calendar/snapshots/restore/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/snapshots/restore/route.ts:43](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/app/api/calendar/snapshots/restore/route.ts#L43)

POST /api/calendar/snapshots/restore?id=<uuid>

Restores the calendar to the snapshot's captured state within the snapshot's
own date range: live events in that range are archived, the snapshot's
events are written back, and all connected clients are notified via
WebSocket broadcasts.

Body `{ eventIds }` restores only those events (see
`DbCalendarSnapshot.restore`); no body restores the whole snapshot.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
