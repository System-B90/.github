[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / getCutStatus

# Function: getCutStatus()

> **getCutStatus**(`curriculumId`): `Promise`\<[`ApiCurriculumCutStatus`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutStatus.md)\>

Defined in: [ui/src/api-server/gantt/cut.ts:1433](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/gantt/cut.ts#L1433)

Report whether a curriculum has live cut events in its linked iteration.
`cut: false` when there is no linked iteration or every cut event was already
pulled back (archived) — either way there is nothing to pull back.

## Parameters

### curriculumId

`string`

## Returns

`Promise`\<[`ApiCurriculumCutStatus`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCurriculumCutStatus.md)\>
