[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/event/export/hive/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/event/export/hive/route.ts:36](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/app/api/event/export/hive/route.ts#L36)

GET /api/event/export/hive — the current schedule as an ICS feed in the
shape Hive's external schedule mode loads (see `api-server/hive/schedule-feed`).

Machine-to-machine: no SSO session, a shared bearer token
(`HIVE_SCHEDULE_FEED_TOKEN`) instead. Unset token = feature off = 404.
Answers `If-None-Match` with 304, so a poller costs one hash per unchanged tick.
Names the file to write in `X-Hive-Calendar-File` when Settings set one.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
