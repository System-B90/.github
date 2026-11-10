[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/syllabuses/\[id\]/shuffles/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/syllabuses/\[id\]/shuffles/route.ts:32](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/app/api/gantt/syllabuses/[id]/shuffles/route.ts#L32)

Lists the modules and events using the shuffle names in `?name=a&name=b`, so
the UI can show what a deletion would strip before it happens (#485).

One param per name because a shuffle name may itself contain a comma; the
comma-joined `?names=a,b` form is still read for older clients.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
