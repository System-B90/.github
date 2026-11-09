[**TypeDoc API**](../../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../../index.md) / [app/api/gantt/curriculums/\[id\]/cut/plan/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/curriculums/\[id\]/cut/plan/route.ts:35](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/app/api/gantt/curriculums/[id]/cut/plan/route.ts#L35)

POST: the "plan" half of the plan-then-confirm cut flow. Runs the full
pipeline (balance → constraints → breaks) and reports what the commit would
do plus the open decisions, without writing anything.

The dialog calls this first, walks the returned `report.decisions` one at a
time, and then POSTs `../cut` with the user's answers.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
