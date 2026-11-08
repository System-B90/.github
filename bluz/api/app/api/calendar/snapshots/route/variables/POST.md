[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/calendar/snapshots/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/snapshots/route.ts:60](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/app/api/calendar/snapshots/route.ts#L60)

POST /api/calendar/snapshots — create a snapshot.
  - `{ label, rangeStart, rangeEnd }` → the server captures the saved events
    inside the range (what the UI sends)
  - `{ label, events }` → stores the supplied events as given

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
