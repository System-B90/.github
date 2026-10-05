[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu](../index.md) / GridContextMenuDeps

# Type Alias: GridContextMenuDeps

> **GridContextMenuDeps** = `object`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:14](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L14)

What the grid lends its right-click menu: every entry reuses a keyboard handler.

## Properties

### allRows

> **allRows**: () => [`GridRow`](../../grid-rows/type-aliases/GridRow.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:17](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L17)

Every summary row open, so subtree entries reach collapsed descendants.

#### Returns

[`GridRow`](../../grid-rows/type-aliases/GridRow.md)[]

***

### events

> **events**: `Record`\<`string`, [`GanttEvent`](../../../../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md) \| `undefined`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:18](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L18)

***

### isEditable

> **isEditable**: (`row`, `col`) => `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:23](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L23)

#### Parameters

##### row

`number`

##### col

`number`

#### Returns

`boolean`

***

### isModuleExpanded

> **isModuleExpanded**: (`key`) => `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:25](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L25)

#### Parameters

##### key

`string`

#### Returns

`boolean`

***

### isSyllabusExpanded

> **isSyllabusExpanded**: (`key`) => `boolean`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:26](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L26)

#### Parameters

##### key

`string`

#### Returns

`boolean`

***

### leadColumns

> **leadColumns**: `number`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:20](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L20)

Columns before the first week (title, sum, courses).

***

### openDialog

> **openDialog**: (`row`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:28](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L28)

#### Parameters

##### row

[`GridRow`](../../grid-rows/type-aliases/GridRow.md)

#### Returns

`void`

***

### placedWeeks

> **placedWeeks**: `ReadonlySet`\<`string`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:24](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L24)

***

### rows

> **rows**: [`GridRow`](../../grid-rows/type-aliases/GridRow.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:15](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L15)

***

### select

> **select**: (`cell`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:22](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L22)

#### Parameters

##### cell

[`GridCell`](../../grid-selection/type-aliases/GridCell.md)

#### Returns

`void`

***

### selection

> **selection**: [`GridSelection`](../../grid-selection/type-aliases/GridSelection.md)

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:21](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L21)

***

### setExpanded

> **setExpanded**: (`row`, `open`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:29](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L29)

#### Parameters

##### row

[`GridRow`](../../grid-rows/type-aliases/GridRow.md)

##### open

`boolean`

#### Returns

`void`

***

### sharedOf

> **sharedOf**: (`row`) => `unknown`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:27](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L27)

#### Parameters

##### row

[`GridRow`](../../grid-rows/type-aliases/GridRow.md)

#### Returns

`unknown`

***

### splitShuffles

> **splitShuffles**: (`eventId`, `moduleId`, `shuffles`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:32](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L32)

#### Parameters

##### eventId

`string`

##### moduleId

`string`

##### shuffles

`string`[]

#### Returns

`Promise`\<`void`\>

***

### startEdit

> **startEdit**: (`row`, `col`) => `void`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:30](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L30)

#### Parameters

##### row

`number`

##### col

`number`

#### Returns

`void`

***

### writeWeek

> **writeWeek**: (`cell`, `minutes`, `zero?`) => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts:31](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/use-grid-context-menu.ts#L31)

#### Parameters

##### cell

[`GridCell`](../../grid-selection/type-aliases/GridCell.md)

##### minutes

`number`

##### zero?

[`ZeroChoice`](../../grid-allotment/type-aliases/ZeroChoice.md)

#### Returns

`Promise`\<`void`\>
