[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/event/history/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/event/history/route.ts:17](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/app/api/event/history/route.ts#L17)

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
