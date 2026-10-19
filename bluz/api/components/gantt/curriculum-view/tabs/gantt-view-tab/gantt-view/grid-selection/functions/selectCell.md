[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection](../index.md) / selectCell

# Function: selectCell()

> **selectCell**(`selection`, `cell`, `mode?`): [`GridSelection`](../type-aliases/GridSelection.md)

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection.ts:40](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection.ts#L40)

Move the cursor to a cell. Plain: select only it. Shift: extend the range
from the anchor. Ctrl: keep the current selection and toggle the cell.

## Parameters

### selection

[`GridSelection`](../type-aliases/GridSelection.md)

### cell

[`GridCell`](../type-aliases/GridCell.md)

### mode?

#### ctrl?

`boolean`

#### shift?

`boolean`

## Returns

[`GridSelection`](../type-aliases/GridSelection.md)
