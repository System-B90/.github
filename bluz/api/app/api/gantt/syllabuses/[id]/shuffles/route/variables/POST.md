[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/syllabuses/\[id\]/shuffles/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/syllabuses/\[id\]/shuffles/route.ts:51](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/app/api/gantt/syllabuses/[id]/shuffles/route.ts#L51)

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
