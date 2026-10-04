[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/use-scroll-to-new-row](../index.md) / useScrollToNewRow

# Function: useScrollToNewRow()

> **useScrollToNewRow**\<`T`\>(`ids`, `containerRef`, `anchorId`): `void`

Defined in: [ui/src/components/base/use-scroll-to-new-row.ts:8](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/base/use-scroll-to-new-row.ts#L8)

Scroll the container to a row whose id newly joined `ids` (a created or
duplicated entry). Rows are found by their DOM `id`, built by `anchorId`.
The first render only records the ids, so opening a list never scrolls.

## Type Parameters

### T

`T` *extends* `string`

## Parameters

### ids

readonly `T`[]

### containerRef

`RefObject`\<`HTMLElement` \| `null`\>

### anchorId

(`id`) => `string`

## Returns

`void`
