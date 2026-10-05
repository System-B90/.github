[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/syllabuses/\[id\]/export/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/syllabuses/\[id\]/export/route.ts:22](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/app/api/gantt/syllabuses/[id]/export/route.ts#L22)

One syllabus as a file (#757): its modules, events and the constraints they
own. `?curriculumId=` names the curriculum whose allocated durations the
import should carry over.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
