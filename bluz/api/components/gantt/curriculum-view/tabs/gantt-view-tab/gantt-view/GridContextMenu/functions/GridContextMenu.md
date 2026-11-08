[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/GridContextMenu](../index.md) / GridContextMenu

# Function: GridContextMenu()

> **GridContextMenu**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/GridContextMenu.tsx:29](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/GridContextMenu.tsx#L29)

The gantt table's right-click menu (#858). Every entry maps onto a handler
the keyboard already uses; this component only renders the list, plus the
value prompt for "set one value for the selected cells".

## Parameters

### \_\_namedParameters

#### onAction

(`action`) => `void`

#### onClose

() => `void`

#### onSetRange

(`text`) => `void`

#### target

[`GridMenuTarget`](../type-aliases/GridMenuTarget.md) \| `null`

## Returns

`Element`
