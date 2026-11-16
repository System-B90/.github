[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / importSyllabusTree

# Function: importSyllabusTree()

> **importSyllabusTree**(`tx`, `source`, `options`): `Promise`\<`string`\>

Defined in: [ui/src/api-server/gantt/import-tree.ts:92](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/gantt/import-tree.ts#L92)

Copies `source` (an exported syllabus tree) under `curriculumId` with fresh
ids. Returns the new syllabus id.

## Parameters

### tx

`PgTransaction`

### source

[`ApiSyllabus`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)

### options

#### curriculumId

`string`

#### maps

[`ImportIdMaps`](../type-aliases/ImportIdMaps.md)

#### now

`Date`

#### titleSuffix?

`string`

## Returns

`Promise`\<`string`\>
