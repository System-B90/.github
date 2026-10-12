[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/SplitCalendarContext](../index.md) / DragStore

# Type Alias: DragStore

> **DragStore** = [`ExternalStore`](../../../../../base/external-store/type-aliases/ExternalStore.md)\<[`ActiveDrag`](ActiveDrag.md) \| `null`\>

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:36](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L36)

The grid drag in flight, outside React state (#955). In the shared context,
a drag start, a drop and every Ctrl/Alt press mid-drag re-rendered every
tile on the grid; now only the dragged event's tiles and the preview do.
