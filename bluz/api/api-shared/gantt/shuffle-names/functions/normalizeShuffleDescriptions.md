[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / normalizeShuffleDescriptions

# Function: normalizeShuffleDescriptions()

> **normalizeShuffleDescriptions**(`descriptions`, `names`): [`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md)

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:58](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/shuffle-names.ts#L58)

Keeps only the descriptions of `names`, trimmed and capped at Hive's limit.
Blank descriptions are dropped so "no description" has one representation.

## Parameters

### descriptions

[`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md) \| `undefined`

### names

`string`[]

## Returns

[`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md)
