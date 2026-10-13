[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/UseDragModifiers](../index.md) / useDragModifiers

# Function: useDragModifiers()

> **useDragModifiers**(`dragging`, `onChange`): () => [`DragModifiers`](../type-aliases/DragModifiers.md)

Defined in: [ui/src/components/schedule/calendar/calendar/UseDragModifiers.ts:53](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/schedule/calendar/calendar/UseDragModifiers.ts#L53)

Live modifier state for react-big-calendar drags, and the reason a modifier
can be pressed mid-drag at all.

The library's `Selection` helper registers a document-level `keydown`
listener at mousedown that *terminates the interaction on any key* — it is
meant for Escape, but it fires for Ctrl and Alt too, so pressing a modifier
once the drag was under way silently ended it (and the auto-repeat of a
modifier held from before the mousedown ended it a moment later). While a
drag is in flight, modifier keydowns are therefore swallowed in the capture
phase on `window`, which runs before the document listener. Escape and every
other key still reach the library untouched.

The drop callbacks carry only computed dates, never the DOM event, so the
modifier state is read from live keyboard/pointer events: `keydown`/`keyup`
always (so a key held before the mousedown is known at drag start), and
`mousemove` while dragging (so a change made with the pointer still is
picked up without waiting for a key event).

## Parameters

### dragging

`boolean` \| (() => `boolean`)

Whether a grid drag is currently in flight, or a live reader
                of it. The reader lets the caller keep the drag out of React
                state (#955): listeners stay attached and ask it per event.

### onChange

(`modifiers`) => `void`

Called with the new modifier set whenever it changes during
                a drag — the caller mirrors it into the drag preview state.

## Returns

A stable reader of the modifiers currently held, drag or no drag.

() => [`DragModifiers`](../type-aliases/DragModifiers.md)
