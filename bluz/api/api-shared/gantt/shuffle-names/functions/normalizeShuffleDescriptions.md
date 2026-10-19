[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / normalizeShuffleDescriptions

# Function: normalizeShuffleDescriptions()

> **normalizeShuffleDescriptions**(`descriptions`, `names`): [`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md)

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:46](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/shuffle-names.ts#L46)

Keeps only the descriptions of `names`, trimmed and capped at Hive's limit.
Blank descriptions are dropped so "no description" has one representation.

## Parameters

### descriptions

[`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md) \| `undefined`

### names

`string`[]

## Returns

[`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md)
