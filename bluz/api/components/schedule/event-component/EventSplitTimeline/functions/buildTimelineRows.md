[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/EventSplitTimeline](../index.md) / buildTimelineRows

# Function: buildTimelineRows()

> **buildTimelineRows**(`pieces`): `TimelineRow`[]

Defined in: [ui/src/components/schedule/event-component/EventSplitTimeline.tsx:31](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/schedule/event-component/EventSplitTimeline.tsx#L31)

Flattens the pieces into an itinerary: every piece is a stop, a working
stretch and a stop; consecutive pieces are joined by a break stretch.

## Parameters

### pieces

readonly [`Interval`](../../../../../api-shared/interval-layout/type-aliases/Interval.md)[]

## Returns

`TimelineRow`[]
