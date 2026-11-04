[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / normalizeShuffleDescriptions

# Function: normalizeShuffleDescriptions()

> **normalizeShuffleDescriptions**(`descriptions`, `names`): [`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md)

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:50](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/gantt/shuffle-names.ts#L50)

Keeps only the descriptions of `names`, trimmed and capped at Hive's limit.
Blank descriptions are dropped so "no description" has one representation.

## Parameters

### descriptions

[`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md) \| `undefined`

### names

`string`[]

## Returns

[`ShuffleDescriptions`](../type-aliases/ShuffleDescriptions.md)
