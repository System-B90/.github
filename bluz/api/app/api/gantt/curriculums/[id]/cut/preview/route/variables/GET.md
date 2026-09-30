[**TypeDoc API**](../../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../../index.md) / [app/api/gantt/curriculums/\[id\]/cut/preview/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/curriculums/\[id\]/cut/preview/route.ts:20](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/app/api/gantt/curriculums/[id]/cut/preview/route.ts#L20)

GET: dry-run cut preview — the planner's dated, timed occurrences for this
curriculum, with no gating and no writes. Used by the bluz CLI
(`curriculums cut-preview`).

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
