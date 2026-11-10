[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/dnd/fast-rect-intersection](../index.md) / createFastRectIntersection

# Function: createFastRectIntersection()

> **createFastRectIntersection**(): `CollisionDetection`

Defined in: [ui/src/components/base/dnd/fast-rect-intersection.ts:160](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/base/dnd/fast-rect-intersection.ts#L160)

dnd-kit's `rectIntersection`, with the same result and a fraction of the
cost, for a `DndContext` with many droppables (the Gantt's day cells).

The droppable rects dnd-kit hands a collision detector are lazy: each
`top`/`left` read re-reads the scroll offset of every scrollable ancestor.
`rectIntersection` makes those reads for every droppable on every pointer
move — tens of thousands of DOM reads a move on a full timeline. Here each
rect is read once per measurement and again only after something scrolled,
which is the only thing that changes what those reads return. The ratio,
its rounding and the order are dnd-kit's own.

It also hands back the *previous* array while the colliding droppables are
unchanged. dnd-kit puts the collisions in the context every draggable and
droppable reads, so a fresh array on every pointer move made React walk the
whole tree under the `DndContext` on every move. Only the ranking is kept,
not the ratios: nothing reads them (the drop target is the first id).

## Returns

`CollisionDetection`

A detector to keep for the lifetime of one `DndContext`.
