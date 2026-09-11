[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/events/\[id\]/recurrence-exceptions/route](../index.md) / DELETE

# Variable: DELETE

> `const` **DELETE**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/events/\[id\]/recurrence-exceptions/route.ts:59](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/api/gantt/events/[id]/recurrence-exceptions/route.ts#L59)

DELETE: Restores a skipped occurrence — the event echoes onto that day
again (#469). A materialized occurrence is not restorable: its standalone
event still occupies the day, so the caller gets a 400 rather than a
silently duplicated block.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
