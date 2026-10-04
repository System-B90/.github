[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/keyboard-drag](../index.md) / neighbourCell

# Function: neighbourCell()

> **neighbourCell**(`cells`, `from`, `direction`): `CellRect` \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/keyboard-drag.ts:34](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/keyboard-drag.ts#L34)

The cell next to `from` in its row (the cells spanning `rowY`), in the
arrow's visual direction (-1 = left, +1 = right). Null at the row's edge.

## Parameters

### cells

readonly `CellRect`[]

### from

#### left

`number`

#### rowY

`number`

### direction

`-1` \| `1`

## Returns

`CellRect` \| `null`
