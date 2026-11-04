[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segments](../index.md) / SegmentDragPreview

# Type Alias: SegmentDragPreview

> **SegmentDragPreview** = [`EventSegment`](EventSegment.md) & `object`

Defined in: [ui/src/components/schedule/calendar/split/segments.ts:57](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/calendar/split/segments.ts#L57)

react-big-calendar's drag layer clones the dragged item and stamps the
proposed `start`/`end` onto the clone (see `EventContainerWrapper.update`).
Those two fields are the only reliable signal that a render is the drag
preview rather than a real grid item — our own segments never carry them.

## Type Declaration

### end

> **end**: `Date`

### start

> **start**: `Date`
