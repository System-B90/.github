[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/use-scroll-to-new-row](../index.md) / useScrollToNewRow

# Function: useScrollToNewRow()

> **useScrollToNewRow**\<`T`\>(`ids`, `containerRef`, `anchorId`): `void`

Defined in: [ui/src/components/base/use-scroll-to-new-row.ts:8](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/base/use-scroll-to-new-row.ts#L8)

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
