[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / importSyllabusTree

# Function: importSyllabusTree()

> **importSyllabusTree**(`tx`, `source`, `options`): `Promise`\<`string`\>

Defined in: [ui/src/api-server/gantt/import-tree.ts:92](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/gantt/import-tree.ts#L92)

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
