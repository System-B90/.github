[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/curriculums/\[id\]/cut/route](../index.md) / DELETE

# Variable: DELETE

> `const` **DELETE**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/curriculums/\[id\]/cut/route.ts:141](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/app/api/gantt/curriculums/[id]/cut/route.ts#L141)

DELETE: pull back a previous cut — soft-delete every live schedule event that
was generated for this curriculum in the linked iteration.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
