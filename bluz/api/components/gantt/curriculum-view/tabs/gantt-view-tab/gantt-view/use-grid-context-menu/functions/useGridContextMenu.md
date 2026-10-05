[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu](../index.md) / useGridContextMenu

# Function: useGridContextMenu()

> **useGridContextMenu**(`deps`): `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:39](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L39)

The gantt table's right-click menu (#858): which entries a cell offers,
and what each one does. Rendering stays in GridContextMenu.

## Parameters

### deps

[`GridContextMenuDeps`](../type-aliases/GridContextMenuDeps.md)

## Returns

`object`

### closeMenu

> **closeMenu**: () => `void`

#### Returns

`void`

### menu

> **menu**: [`GridMenuState`](../type-aliases/GridMenuState.md) \| `null`

### openMenu

> **openMenu**: (`e`, `cell`) => `void`

#### Parameters

##### e

`MouseEvent`\<`HTMLElement`\>

##### cell

[`GridCell`](../../grid-selection/type-aliases/GridCell.md)

#### Returns

`void`

### runMenuAction

> **runMenuAction**: (`action`) => `void`

#### Parameters

##### action

`"copy"` \| `"clear-week"` \| `"collapse-all-under"` \| `"collapse"` \| `"edit-week"` \| `"expand-all-under"` \| `"expand"` \| `"open-dialog"` \| `"remove-mapping"` \| `"split-shuffles"`

#### Returns

`void`

### setRange

> **setRange**: (`text`) => `Promise`\<`void`\>

#### Parameters

##### text

`string`

#### Returns

`Promise`\<`void`\>
