[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-context-menu](../index.md) / summaryRowsUnder

# Function: summaryRowsUnder()

> **summaryRowsUnder**(`allRows`, `targetKey`): [`GridRow`](../../grid-rows/type-aliases/GridRow.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-context-menu.ts:69](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-context-menu.ts#L69)

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
