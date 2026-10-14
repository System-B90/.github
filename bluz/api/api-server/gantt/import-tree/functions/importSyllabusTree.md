[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / importSyllabusTree

# Function: importSyllabusTree()

> **importSyllabusTree**(`tx`, `source`, `options`): `Promise`\<`string`\>

Defined in: [ui/src/api-server/gantt/import-tree.ts:88](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-server/gantt/import-tree.ts#L88)

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
