[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/dnd/SortableTableRow](../index.md) / SortableTableRow

# Function: SortableTableRow()

> **SortableTableRow**(`__namedParameters`): `Element`

Defined in: [ui/src/components/base/dnd/SortableTableRow.tsx:27](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/dnd/SortableTableRow.tsx#L27)

A table row that is a dnd-kit sortable item, with `useSortable` confined to
the row element and its handle cell.

dnd-kit re-renders every sortable item whenever the item under the drag
changes. In the component that also builds the row's cells — text fields,
selects, instructor pickers — that rebuilt every row of the list at each
step of a sort. The other cells arrive as `children`, created by a caller
the sort does not re-render, so React reuses them as they are.

## Parameters

### \_\_namedParameters

[`SortableTableRowProps`](../type-aliases/SortableTableRowProps.md)

## Returns

`Element`
