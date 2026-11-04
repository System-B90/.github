[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / normalizeShuffleDescriptions

# Function: normalizeShuffleDescriptions()

> **normalizeShuffleDescriptions**(`descriptions`, `names`): [`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md)

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:50](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/shuffle-names.ts#L50)

Keeps only the descriptions of `names`, trimmed and capped at Hive's limit.
Blank descriptions are dropped so "no description" has one representation.

## Parameters

### descriptions

[`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md) \| `undefined`

### names

`string`[]

## Returns

[`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md)
