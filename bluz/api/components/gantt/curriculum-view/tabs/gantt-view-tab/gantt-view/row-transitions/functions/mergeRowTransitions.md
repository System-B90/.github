[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/row-transitions](../index.md) / mergeRowTransitions

# Function: mergeRowTransitions()

> **mergeRowTransitions**(`previous`, `next`): [`TransitionRow`](../type-aliases/TransitionRow.md)[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/row-transitions.ts:13](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/row-transitions.ts#L13)

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
