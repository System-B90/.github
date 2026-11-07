[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/dnd/fast-rect-intersection](../index.md) / createFastPointerWithin

# Function: createFastPointerWithin()

> **createFastPointerWithin**(): `CollisionDetection`

Defined in: [ui/src/components/base/dnd/fast-rect-intersection.ts:174](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/base/dnd/fast-rect-intersection.ts#L174)

dnd-kit's `pointerWithin`, with the same caching as
[createFastRectIntersection](createFastRectIntersection.md). For drags aimed with the pointer rather
than with the dragged box: the schedule's instructor chips, whose wide
overlay used to graze a neighbouring tile and turn a drop on empty space
into a move. Falls back to rect intersection when there is no pointer.

## Returns

`CollisionDetection`

A detector to keep for the lifetime of one `DndContext`.
