[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/EventSplitTimeline](../index.md) / EventSplitTimeline

# Function: EventSplitTimeline()

> **EventSplitTimeline**(`activePiece`): `Element`

Defined in: [ui/src/components/schedule/event-component/EventSplitTimeline.tsx:79](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/event-component/EventSplitTimeline.tsx#L79)

The tooltip's itinerary for an event split across breaks. Time flows top to
bottom like the day view it came from: a solid rail for each working piece,
a dotted rail for each break. Filled dots mark the event's true start and
end; hollow dots mark where it pauses and resumes.

## Parameters

### activePiece

The piece under the pointer; its rail, times and
       length are drawn bold. Every other row stays as it is.

#### activePiece?

`number`

#### pieces

readonly [`Interval`](../../../../../api-shared/interval-layout/type-aliases/Interval.md)[]

## Returns

`Element`
