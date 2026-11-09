[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/calendar/drafts/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/drafts/route.ts:45](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/app/api/calendar/drafts/route.ts#L45)

GET /api/calendar/drafts
  - no params  → list shared drafts (summaries, newest-updated first)
  - ?id=<uuid> → fetch one draft including its events (to load it)

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
