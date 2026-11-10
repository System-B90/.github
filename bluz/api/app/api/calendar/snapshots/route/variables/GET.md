[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/calendar/snapshots/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/snapshots/route.ts:33](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/app/api/calendar/snapshots/route.ts#L33)

GET /api/calendar/snapshots
  - no params  → list snapshots (summaries, newest first)
  - ?id=<uuid> → fetch one snapshot including its captured events (for restore)

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
