[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/SplitCalendarContext](../index.md) / SplitCalendarContextValue

# Type Alias: SplitCalendarContextValue

> **SplitCalendarContextValue** = `object`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:28](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L28)

Shared state that makes the separate grid boxes of one split event behave as
a single object: hovering, selecting or dragging any piece lights up all of
them, and the drag preview can re-lay-out the whole event live because the
break windows travel with the context.

## Properties

### activeDrag

> **activeDrag**: [`ActiveDrag`](ActiveDrag.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:30](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L30)

***

### breakWindows

> **breakWindows**: `ReadonlyArray`\<[`BreakWindow`](../../../../../../api-shared/break-windows/type-aliases/BreakWindow.md)\>

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:29](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L29)

***

### hoveredEventId

> **hoveredEventId**: [`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L31)

***

### openContextMenu

> **openContextMenu**: `null` \| [`OpenEventContextMenu`](OpenEventContextMenu.md)

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:45](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L45)

`null` while the calendar is read-only — a past iteration has nothing to
offer a menu whose every entry is a write, and the tiles then leave the
browser's own menu alone.

***

### selectedEventId

> **selectedEventId**: [`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:32](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L32)

***

### selectedEventIds

> **selectedEventIds**: `ReadonlySet`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)\>

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:38](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L38)

Events the user has Ctrl/Cmd+clicked into a multi-selection (#706). The
tiles draw a selection ring for these exactly as for `selectedEventId`,
so a selection of many reads like a selection of one.

***

### setHoveredEventId

> **setHoveredEventId**: (`eventId`) => `void`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:39](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L39)

#### Parameters

##### eventId

[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md) \| `null`

#### Returns

`void`

***

### splitEventAt

> **splitEventAt**: (`event`, `atMs`) => `void`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:47](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L47)

Middle-click / Shift+click on a tile: cut the event in two at `atMs` (#657).

#### Parameters

##### event

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

##### atMs

`number`

#### Returns

`void`
