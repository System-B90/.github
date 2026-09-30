[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/curriculums/\[id\]/execution/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/curriculums/\[id\]/execution/route.ts:20](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/app/api/gantt/curriculums/[id]/execution/route.ts#L20)

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
