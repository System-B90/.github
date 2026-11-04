[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/event/history/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/event/history/route.ts:17](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/app/api/event/history/route.ts#L17)

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
