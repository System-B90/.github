[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/calendar/drafts/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/drafts/route.ts:44](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/app/api/calendar/drafts/route.ts#L44)

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
