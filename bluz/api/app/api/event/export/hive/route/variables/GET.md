[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/event/export/hive/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/event/export/hive/route.ts:32](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/app/api/event/export/hive/route.ts#L32)

GET /api/event/export/hive — the current schedule as an ICS feed in the
shape Hive's external schedule mode loads (see `api-server/hive/schedule-feed`).

Machine-to-machine: no SSO session, a shared bearer token
(`HIVE_SCHEDULE_FEED_TOKEN`) instead. Unset token = feature off = 404.
Answers `If-None-Match` with 304, so a poller costs one hash per unchanged tick.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
