[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / importSyllabusTree

# Function: importSyllabusTree()

> **importSyllabusTree**(`tx`, `source`, `options`): `Promise`\<`string`\>

Defined in: [ui/src/api-server/gantt/import-tree.ts:90](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/import-tree.ts#L90)

Copies `source` (an exported syllabus tree) under `curriculumId` with fresh
ids. Allocated durations come from the config the export held for
`sourceCurriculumId`. Returns the new syllabus id.

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

#### sourceCurriculumId

`string` \| `undefined`

#### titleSuffix?

`string`

## Returns

`Promise`\<`string`\>
