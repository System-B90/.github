[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [app/api/gantt/curriculums/\[id\]/import-syllabus/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/gantt/curriculums/\[id\]/import-syllabus/route.ts:27](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/app/api/gantt/curriculums/[id]/import-syllabus/route.ts#L27)

Adds a syllabus exported with `/api/gantt/syllabuses/{id}/export` to this
curriculum as a new copy (#757). Returns the full syllabus tree.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
