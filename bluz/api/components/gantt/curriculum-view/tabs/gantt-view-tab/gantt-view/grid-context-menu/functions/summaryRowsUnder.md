[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-context-menu](../index.md) / summaryRowsUnder

# Function: summaryRowsUnder()

> **summaryRowsUnder**(`allRows`, `targetKey`): [`GridRow`](../../grid-rows/type-aliases/GridRow.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-context-menu.ts:69](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-context-menu.ts#L69)

Summary rows at and under `targetKey`, read from a fully opened build so
collapsed descendants are included.

## Parameters

### allRows

[`GridRow`](../../grid-rows/type-aliases/GridRow.md)[]

Rows built with every syllabus/shuffle/module open.

### targetKey

`string`

The right-clicked summary row's key.

## Returns

[`GridRow`](../../grid-rows/type-aliases/GridRow.md)[]
