[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/curriculums/\[id\]/execution/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/curriculums/\[id\]/execution/route.ts:20](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/app/api/gantt/curriculums/[id]/execution/route.ts#L20)

GET: תכנון מול ביצוע — computed-on-read comparison between the curriculum's
gantt plan and the schedule events cut from it. Not-yet-cut curriculums
(or ones with no linked iteration) return `{ events: {} }` with a 200.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
