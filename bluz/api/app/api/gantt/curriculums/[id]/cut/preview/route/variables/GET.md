[**TypeDoc API**](../../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../../index.md) / [app/api/gantt/curriculums/\[id\]/cut/preview/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/curriculums/\[id\]/cut/preview/route.ts:22](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/app/api/gantt/curriculums/[id]/cut/preview/route.ts#L22)

GET: dry-run cut preview — the planner's dated, timed occurrences for this
curriculum, with no gating and no writes. Used by the bluz CLI
(`curriculums cut-preview`). `?template=<id>` previews under that week
template, `?parkNonTemplate=true` parks what the template does not place.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
