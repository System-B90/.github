[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/SplitCalendarContext](../index.md) / SplitCalendarContextValue

# Type Alias: SplitCalendarContextValue

> **SplitCalendarContextValue** = `object`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L21)

Shared state that makes the separate grid boxes of one split event behave as
a single object: hovering, selecting or dragging any piece lights up all of
them, and the drag preview can re-lay-out the whole event live because the
break windows travel with the context.

## Properties

### activeDrag

> **activeDrag**: [`ActiveDrag`](ActiveDrag.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L23)

***

### breakWindows

> **breakWindows**: `ReadonlyArray`\<[`BreakWindow`](../../../../../../api-shared/break-windows/type-aliases/BreakWindow.md)\>

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:22](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L22)

***

### hoveredEventId

> **hoveredEventId**: [`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L24)

***

### selectedEventId

> **selectedEventId**: [`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L25)

***

### setHoveredEventId

> **setHoveredEventId**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L26)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md) \| `null`

#### Returns

`void`

***

### splitEventAt

> **splitEventAt**: (`event`, `atMs`) => `void`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L28)

Middle-click / Shift+click on a tile: cut the event in two at `atMs` (#657).

#### Parameters

##### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

##### atMs

`number`

#### Returns

`void`
