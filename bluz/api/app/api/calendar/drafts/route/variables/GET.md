[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/calendar/drafts/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/drafts/route.ts:42](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/app/api/calendar/drafts/route.ts#L42)

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
