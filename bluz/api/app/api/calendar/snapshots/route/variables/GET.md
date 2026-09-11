[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/calendar/snapshots/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/snapshots/route.ts:31](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/api/calendar/snapshots/route.ts#L31)

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
