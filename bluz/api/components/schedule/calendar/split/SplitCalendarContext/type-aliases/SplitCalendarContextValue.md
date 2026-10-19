[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/SplitCalendarContext](../index.md) / SplitCalendarContextValue

# Type Alias: SplitCalendarContextValue

> **SplitCalendarContextValue** = `object`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:66](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L66)

Shared state that makes the separate grid boxes of one split event behave as
a single object: hovering, selecting or dragging any piece lights up all of
them, and the drag preview can re-lay-out the whole event live because the
break windows travel with the context.

Volatile interaction state (hover, drag, single selection) is held in
stores whose identity never changes, so changing it never changes this
value; tiles read it through the per-event hooks below.

## Properties

### breakWindows

> **breakWindows**: `ReadonlyArray`\<[`BreakWindow`](../../../../../../api-shared/break-windows/type-aliases/BreakWindow.md)\>

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:67](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L67)

***

### drag

> **drag**: [`DragStore`](DragStore.md)

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:68](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L68)

***

### hover

> **hover**: [`HoverStore`](HoverStore.md)

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:69](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L69)

***

### openContextMenu

> **openContextMenu**: `null` \| [`OpenEventContextMenu`](OpenEventContextMenu.md)

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:82](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L82)

`null` leaves the browser's own menu alone. The calendar always supplies
one: on a past iteration its write entries are disabled but Copy still
works, to carry an event into a writable iteration (#859).

***

### selectedEventIds

> **selectedEventIds**: `ReadonlySet`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)\>

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:76](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L76)

Events the user has Ctrl/Cmd+clicked into a multi-selection (#706). The
tiles draw a selection ring for these exactly as for the single
selection, so a selection of many reads like a selection of one.

***

### selection

> **selection**: [`SelectionStore`](SelectionStore.md)

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:70](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L70)

***

### slotContextMenuEnabled

> **slotContextMenuEnabled**: `boolean`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:86](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L86)

Right-click on empty grid opens the paste menu (#859).

***

### splitEventAt

> **splitEventAt**: (`event`, `atMs`) => `void`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:84](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L84)

Middle-click / Shift+click on a tile: cut the event in two at `atMs` (#657).

#### Parameters

##### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

##### atMs

`number`

#### Returns

`void`
