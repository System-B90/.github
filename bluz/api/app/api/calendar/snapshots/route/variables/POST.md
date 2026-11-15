[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/calendar/snapshots/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/snapshots/route.ts:60](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/app/api/calendar/snapshots/route.ts#L60)

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
