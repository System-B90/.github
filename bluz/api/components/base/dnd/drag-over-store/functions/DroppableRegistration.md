[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/dnd/drag-over-store](../index.md) / DroppableRegistration

# Function: DroppableRegistration()

> **DroppableRegistration**(`__namedParameters`): `null`

Defined in: [ui/src/components/base/dnd/drag-over-store.tsx:174](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/base/dnd/drag-over-store.tsx#L174)

Registers the element behind `slot` as a dnd-kit droppable.

dnd-kit only registers droppables through `useDroppable`, whose caller
re-renders on every change to the drag. Calling it here, in a component
that renders nothing, keeps that cost off the element itself: it reads
whether the drag is over it through [useIsDragOver](useIsDragOver.md) instead.

## Parameters

### \_\_namedParameters

`UseDroppableArguments` & `object`

## Returns

`null`
