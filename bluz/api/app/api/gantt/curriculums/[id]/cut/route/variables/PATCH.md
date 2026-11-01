[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/curriculums/\[id\]/cut/route](../index.md) / PATCH

# Variable: PATCH

> `const` **PATCH**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/curriculums/\[id\]/cut/route.ts:118](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/app/api/gantt/curriculums/[id]/cut/route.ts#L118)

PATCH: reload an already-cut schedule from the current gantt — add new
occurrences, retime changed ones, archive dropped ones. Manually edited
events are skipped and reported as conflicts unless listed in
`overrideEventIds`. `dryRun` returns the same diff without writing.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
