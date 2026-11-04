[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/dnd/DraggableBox](../index.md) / DraggableBox

# Function: DraggableBox()

> **DraggableBox**(`__namedParameters`): `Element`

Defined in: [ui/src/components/base/dnd/DraggableBox.tsx:63](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/base/dnd/DraggableBox.tsx#L63)

A `Box` that is a dnd-kit draggable, with `useDraggable` confined to it.

dnd-kit re-renders every `useDraggable` caller whenever the droppable under
the drag changes. Called by the component that also builds an item's
content — tooltip, avatar, labels, store lookups — it rebuilt all of that
for every item on screen at each crossing. Here only this element
re-renders: `children` are created by the caller, which a drag does not
re-render, so React reuses them as they are.

## Parameters

### \_\_namedParameters

[`DraggableBoxProps`](../type-aliases/DraggableBoxProps.md)

## Returns

`Element`
