[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/shuffles](../index.md) / apiApplyShuffles

# Function: apiApplyShuffles()

> **apiApplyShuffles**(`syllabusId`, `shuffles`, `descriptions?`): `Promise`\<[`ShuffleUsages`](../../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\>

Defined in: [ui/src/api-client/gantt/shuffles.ts:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/gantt/shuffles.ts#L27)

Replaces the syllabus' shuffle list, stripping every removed name off the
modules and events that carry it. Returns what was stripped. Omitting
`descriptions` keeps the surviving names' current descriptions.

## Parameters

### syllabusId

`string`

### shuffles

`string`[]

### descriptions?

[`ShuffleDescriptions`](../../../../api-shared/gantt/shuffle-names/type-aliases/ShuffleDescriptions.md)

## Returns

`Promise`\<[`ShuffleUsages`](../../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\>
