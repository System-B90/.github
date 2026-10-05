[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection](../index.md) / GridSelection

# Type Alias: GridSelection

> **GridSelection** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection.ts:7](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection.ts#L7)

Spreadsheet selection: the range from anchor to cursor, plus cells kept
from earlier Ctrl+click ranges.

## Properties

### anchor

> **anchor**: [`GridCell`](GridCell.md) \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection.ts:9](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection.ts#L9)

Null after Ctrl+click deselects a cell: the cursor sits there with no range.

***

### cursor

> **cursor**: [`GridCell`](GridCell.md)

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection.ts:10](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection.ts#L10)

***

### extra

> **extra**: `Set`\<`string`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection.ts:11](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-selection.ts#L11)
