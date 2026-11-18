[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/dnd/SortableTableRow](../index.md) / SortableTableRowProps

# Type Alias: SortableTableRowProps

> **SortableTableRowProps** = `Omit`\<`TableRowProps`, `"ref"`\> & `object`

Defined in: [ui/src/components/base/dnd/SortableTableRow.tsx:10](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/base/dnd/SortableTableRow.tsx#L10)

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
