[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/dnd/drag-over-store](../index.md) / DragOverState

# Type Alias: DragOverState

> **DragOverState** = `object`

Defined in: [ui/src/components/base/dnd/drag-over-store.tsx:38](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/dnd/drag-over-store.tsx#L38)

The drag in flight inside one `DndContext`, as its drop targets read it.

dnd-kit hands every `useDroppable` and `useDraggable` caller its whole
internal context, which changes whenever the droppable under the pointer
does. With a drop target per Gantt day cell and per schedule tile, each of
those crossings re-rendered every cell, row, bar and tile on screen. Drop
targets register through [DroppableRegistration](../functions/DroppableRegistration.md), a leaf that renders
nothing, and read whether they are under the drag from this store, so a
crossing re-renders only the target the drag left and the one it entered.

## Properties

### active

> **active**: \{ `data`: `Data` \| `undefined`; `id`: `UniqueIdentifier`; \} \| `null`

Defined in: [ui/src/components/base/dnd/drag-over-store.tsx:40](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/dnd/drag-over-store.tsx#L40)

The dragged item, or null when nothing is being dragged.

***

### overId

> **overId**: `null` \| `UniqueIdentifier`

Defined in: [ui/src/components/base/dnd/drag-over-store.tsx:42](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/dnd/drag-over-store.tsx#L42)

The droppable currently under the drag, if any.
