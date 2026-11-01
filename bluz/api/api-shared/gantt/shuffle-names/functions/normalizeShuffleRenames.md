[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/shuffle-names](../index.md) / normalizeShuffleRenames

# Function: normalizeShuffleRenames()

> **normalizeShuffleRenames**(`renames`): [`ShuffleRenames`](../type-aliases/ShuffleRenames.md)

Defined in: [ui/src/api-shared/gantt/shuffle-names.ts:89](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/gantt/shuffle-names.ts#L89)

Normalizes a rename map, dropping blank or no-op entries so "renamed to
itself" never cascades a write.

## Parameters

### renames

[`ShuffleRenames`](../type-aliases/ShuffleRenames.md) \| `undefined`

## Returns

[`ShuffleRenames`](../type-aliases/ShuffleRenames.md)
