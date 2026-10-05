[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / normalizeShuffleRenames

# Function: normalizeShuffleRenames()

> **normalizeShuffleRenames**(`renames`): [`ShuffleRenames`](../type-aliases/ShuffleRenames.md)

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:82](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/gantt/shuffle-names.ts#L82)

Normalizes a rename map, dropping blank or no-op entries so "renamed to
itself" never cascades a write.

## Parameters

### renames

[`ShuffleRenames`](../type-aliases/ShuffleRenames.md) \| `undefined`

## Returns

[`ShuffleRenames`](../type-aliases/ShuffleRenames.md)
