[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/syllabuses/\[id\]/shuffles/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/syllabuses/\[id\]/shuffles/route.ts:50](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/app/api/gantt/syllabuses/[id]/shuffles/route.ts#L50)

Applies the new shuffle list, cascading removals onto modules and events.
An optional `descriptions` (name → text) replaces the shuffle descriptions.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
