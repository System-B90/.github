[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/dnd/SortableTableRow](../index.md) / SortableTableRowProps

# Type Alias: SortableTableRowProps

> **SortableTableRowProps** = `Omit`\<`TableRowProps`, `"ref"`\> & `object`

Defined in: [ui/src/components/base/dnd/SortableTableRow.tsx:10](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/base/dnd/SortableTableRow.tsx#L10)

## Type Declaration

### handle

> **handle**: (`props`) => `ReactNode`

The drag-handle cell. Rendered here on every change to the sort, so keep it small.

#### Parameters

##### props

[`SortableHandleProps`](SortableHandleProps.md)

#### Returns

`ReactNode`

### sortable

> **sortable**: `UseSortableArguments`

What `useSortable` registers.
