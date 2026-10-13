[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/shuffle-alignment](../index.md) / shuffleAlignmentWarning

# Function: shuffleAlignmentWarning()

> **shuffleAlignmentWarning**(`moves`, `sources`): `string` \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/shuffle-alignment.ts:98](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/shuffle-alignment.ts#L98)

Why `moves` would misalign a syllabus's shuffles on some day, or null.
Only a day that was aligned and no longer is counts; an existing
imbalance is not this drop's doing. Runs per hovered cell, so the
mappings are indexed by day once per call rather than once per check.
It reports the first broken day only: the cell warning is a hint.

## Parameters

### moves

[`EventMove`](../type-aliases/EventMove.md)[]

### sources

[`AlignmentSources`](../type-aliases/AlignmentSources.md)

## Returns

`string` \| `null`
