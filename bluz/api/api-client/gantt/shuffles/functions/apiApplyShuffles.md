[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/shuffles](../index.md) / apiApplyShuffles

# Function: apiApplyShuffles()

> **apiApplyShuffles**(`syllabusId`, `shuffles`, `descriptions?`, `renames?`): `Promise`\<[`ShuffleUsages`](../../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\>

Defined in: [ui/src/api-client/gantt/shuffles.ts:28](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-client/gantt/shuffles.ts#L28)

Replaces the syllabus' shuffle list, stripping every removed name off the
modules and events that carry it and rewriting renamed ones (#774).
Returns what was retagged. Omitting `descriptions` keeps the surviving
names' current descriptions.

## Parameters

### syllabusId

`string`

### shuffles

`string`[]

### descriptions?

[`ShuffleDescriptions`](../../../../api-shared/gantt/shuffle-names/type-aliases/ShuffleDescriptions.md)

### renames?

[`ShuffleRenames`](../../../../api-shared/gantt/shuffle-names/type-aliases/ShuffleRenames.md)

## Returns

`Promise`\<[`ShuffleUsages`](../../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\>
