[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/sort-order](../index.md) / nextModuleSortOrder

# Function: nextModuleSortOrder()

> **nextModuleSortOrder**(`syllabusId`): `SQL`

Defined in: [ui/src/api-server/gantt/sort-order.ts:17](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/gantt/sort-order.ts#L17)

`sort_order` for a module appended to `syllabusId`: one past the current
last. Linking with the column default (0) put new rows at the top after a
reload, so a saved order looked lost (#761).

## Parameters

### syllabusId

`string`

## Returns

`SQL`
