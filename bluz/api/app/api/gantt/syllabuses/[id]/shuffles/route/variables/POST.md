[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/syllabuses/\[id\]/shuffles/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/syllabuses/\[id\]/shuffles/route.ts:53](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/app/api/gantt/syllabuses/[id]/shuffles/route.ts#L53)

Applies the new shuffle list, cascading removals onto modules and events.
An optional `descriptions` (name → text) replaces the shuffle descriptions;
an optional `renames` (old → new name) rewrites the tags that use them (#774).

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
