[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/EventSplitTimeline](../index.md) / buildTimelineRows

# Function: buildTimelineRows()

> **buildTimelineRows**(`pieces`): `TimelineRow`[]

Defined in: [ui/src/components/schedule/event-component/EventSplitTimeline.tsx:31](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/event-component/EventSplitTimeline.tsx#L31)

Flattens the pieces into an itinerary: every piece is a stop, a working
stretch and a stop; consecutive pieces are joined by a break stretch.

## Parameters

### pieces

readonly [`Interval`](../../../../../api-shared/interval-layout/type-aliases/Interval.md)[]

## Returns

`TimelineRow`[]
