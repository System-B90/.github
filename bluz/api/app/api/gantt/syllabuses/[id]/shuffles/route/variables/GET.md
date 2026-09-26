[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/syllabuses/\[id\]/shuffles/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/syllabuses/\[id\]/shuffles/route.ts:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/app/api/gantt/syllabuses/[id]/shuffles/route.ts#L31)

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
