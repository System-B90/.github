[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/event/history/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/event/history/route.ts:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/api/event/history/route.ts#L17)

GET /api/event/history?id=<eventId> — the change log of a single event
("היסטוריית שינויים"), newest first. Read-only: rows are written by the
write paths themselves (see `api-server/db-event-history.ts`).

## Parameters

### request

`NextRequest`

### context?

`any`

## Returns

`Promise`\<`Response`\>
