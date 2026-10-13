[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/SplitCalendarContext](../index.md) / HoverStore

# Type Alias: HoverStore

> **HoverStore** = [`ExternalStore`](../../../../../base/external-store/type-aliases/ExternalStore.md)\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md) \| `null`\>

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:25](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L25)

Which event the pointer is over, outside React state (#924). Held as
`CalendarView` state, every enter/leave re-rendered the whole calendar and
every tile; now only the tiles whose hovered-ness flips re-render.
