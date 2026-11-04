[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/stable-drag-and-drop](../index.md) / withStableDragAndDrop

# Function: withStableDragAndDrop()

> **withStableDragAndDrop**\<`TEvent`, `TResource`\>(`Calendar`): `ComponentType`\<[`StableDragAndDropProps`](../type-aliases/StableDragAndDropProps.md)\<`TEvent`, `TResource`\>\>

Defined in: [ui/src/components/schedule/calendar/calendar/stable-drag-and-drop.tsx:120](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/calendar/calendar/stable-drag-and-drop.tsx#L120)

react-big-calendar's `withDragAndDrop`, rebuilt so the drag layer does not
re-render the calendar underneath it.

The addon keeps its drag state on the wrapper and renders the calendar
straight from it, so a mousedown on a tile (even a plain click), the drag
actually starting, and the drop each re-rendered the whole grid: every
time slot, every column's layout pass and every tile. It also rebuilt its
`components` map on each of those renders, which would remount any custom
container wrapper outright.

Here the calendar is memoised and its props stay put for the length of a
drag. The drag state reaches the addon's own wrappers (tiles, columns, week
rows) through its context, the only place it is read, and the "dragging"
class is toggled on the root element rather than rendered into it. The
wrappers, `Selection` and the drop callbacks are the addon's own, unchanged.

## Type Parameters

### TEvent

`TEvent` *extends* `object`

### TResource

`TResource` *extends* `object`

## Parameters

### Calendar

`ComponentType`\<`CalendarProps`\<`TEvent`, `TResource`\>\>

The calendar to put the drag layer over.

## Returns

`ComponentType`\<[`StableDragAndDropProps`](../type-aliases/StableDragAndDropProps.md)\<`TEvent`, `TResource`\>\>

A drop-in replacement for `withDragAndDrop(Calendar)`.
