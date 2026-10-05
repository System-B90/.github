[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/drizzle-normalize](../index.md) / normalizeApiSyllabus

# Function: normalizeApiSyllabus()

> **normalizeApiSyllabus**(`rawSyllabus`, `curriculumId`): [`NormalizedSyllabusSubtree`](../type-aliases/NormalizedSyllabusSubtree.md)

Defined in: [ui/src/api-client/gantt/drizzle-normalize.ts:62](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-client/gantt/drizzle-normalize.ts#L62)

Flattens one `ApiSyllabus` (with nested `s2m → module → m2e → event`) into
normalized store slices, resolving the reverse child-id arrays.

## Parameters

### rawSyllabus

[`ApiSyllabus`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)

### curriculumId

`string`

## Returns

[`NormalizedSyllabusSubtree`](../type-aliases/NormalizedSyllabusSubtree.md)
