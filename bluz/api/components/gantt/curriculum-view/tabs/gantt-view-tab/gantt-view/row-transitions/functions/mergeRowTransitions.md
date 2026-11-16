[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/row-transitions](../index.md) / mergeRowTransitions

# Function: mergeRowTransitions()

> **mergeRowTransitions**(`previous`, `next`): [`TransitionRow`](../type-aliases/TransitionRow.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/row-transitions.ts:13](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/row-transitions.ts#L13)

Display rows while a collapse/expand animates: the new rows, the ones that
just appeared marked `enter`, and the ones that just vanished kept in place
as `exit` until the caller drops them. Rows keep their relative order.

## Parameters

### previous

[`GridRow`](../../grid-rows/type-aliases/GridRow.md)[]

### next

[`GridRow`](../../grid-rows/type-aliases/GridRow.md)[]

## Returns

[`TransitionRow`](../type-aliases/TransitionRow.md)[]
