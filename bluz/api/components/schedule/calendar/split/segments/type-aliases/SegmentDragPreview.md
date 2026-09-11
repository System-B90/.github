[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segments](../index.md) / SegmentDragPreview

# Type Alias: SegmentDragPreview

> **SegmentDragPreview** = [`EventSegment`](EventSegment.md) & `object`

Defined in: [ui/src/components/schedule/calendar/split/segments.ts:54](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/split/segments.ts#L54)

react-big-calendar's drag layer clones the dragged item and stamps the
proposed `start`/`end` onto the clone (see `EventContainerWrapper.update`).
Those two fields are the only reliable signal that a render is the drag
preview rather than a real grid item — our own segments never carry them.

## Type Declaration

### end

> **end**: `Date`

### start

> **start**: `Date`
