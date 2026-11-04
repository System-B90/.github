[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/base](../index.md) / BluzEventComponent

# Variable: BluzEventComponent

> `const` **BluzEventComponent**: `NamedExoticComponent`\<`EventProps`\<[`EventSegment`](../../../calendar/split/segments/type-aliases/EventSegment.md)\>\>

Defined in: [ui/src/components/schedule/event-component/base.tsx:147](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/schedule/event-component/base.tsx#L147)

react-big-calendar's `components.event`. The grid feeds it segments — one
box per drawn piece of an event — and it renders either a real grid piece or
the live drag preview of the whole event.

Memoised on the segment alone, the only prop it reads. The grid hands every
tile a fresh `localizer`, `title` and slot bounds on each render, so without
this a drop (or any websocket upsert) re-rendered every tile in view, not
just the ones whose segments changed. Segments keep their identity while
their event does (#927); interaction state reaches tiles through stores.
