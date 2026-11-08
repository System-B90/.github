[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / normalizeShuffleRenames

# Function: normalizeShuffleRenames()

> **normalizeShuffleRenames**(`renames`): [`ShuffleRenames`](../type-aliases/ShuffleRenames.md)

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:97](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/gantt/shuffle-names.ts#L97)

Normalizes a rename map, dropping blank or no-op entries so "renamed to
itself" never cascades a write.

## Parameters

### renames

[`ShuffleRenames`](../type-aliases/ShuffleRenames.md) \| `undefined`

## Returns

[`ShuffleRenames`](../type-aliases/ShuffleRenames.md)
