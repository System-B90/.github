[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/drizzle-normalize](../index.md) / normalizeApiSyllabus

# Function: normalizeApiSyllabus()

> **normalizeApiSyllabus**(`rawSyllabus`, `curriculumId`): [`NormalizedSyllabusSubtree`](../type-aliases/NormalizedSyllabusSubtree.md)

Defined in: [ui/src/api-client/gantt/drizzle-normalize.ts:62](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-client/gantt/drizzle-normalize.ts#L62)

Flattens one `ApiSyllabus` (with nested `s2m → module → m2e → event`) into
normalized store slices, resolving the reverse child-id arrays.

## Parameters

### rawSyllabus

[`ApiSyllabus`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)

### curriculumId

`string`

## Returns

[`NormalizedSyllabusSubtree`](../type-aliases/NormalizedSyllabusSubtree.md)
