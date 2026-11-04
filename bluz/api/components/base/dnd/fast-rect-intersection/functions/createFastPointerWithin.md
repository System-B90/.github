[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/base/dnd/fast-rect-intersection](../index.md) / createFastPointerWithin

# Function: createFastPointerWithin()

> **createFastPointerWithin**(): `CollisionDetection`

Defined in: [ui/src/components/base/dnd/fast-rect-intersection.ts:174](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/base/dnd/fast-rect-intersection.ts#L174)

dnd-kit's `pointerWithin`, with the same caching as
[createFastRectIntersection](createFastRectIntersection.md). For drags aimed with the pointer rather
than with the dragged box: the schedule's instructor chips, whose wide
overlay used to graze a neighbouring tile and turn a drop on empty space
into a move. Falls back to rect intersection when there is no pointer.

## Returns

`CollisionDetection`

A detector to keep for the lifetime of one `DndContext`.
