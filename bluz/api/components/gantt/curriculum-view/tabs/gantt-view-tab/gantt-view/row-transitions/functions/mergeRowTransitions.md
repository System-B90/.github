[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/row-transitions](../index.md) / mergeRowTransitions

# Function: mergeRowTransitions()

> **mergeRowTransitions**(`previous`, `next`): [`TransitionRow`](../type-aliases/TransitionRow.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/row-transitions.ts:13](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/row-transitions.ts#L13)

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
