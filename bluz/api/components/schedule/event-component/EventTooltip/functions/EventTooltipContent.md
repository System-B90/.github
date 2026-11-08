[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/EventTooltip](../index.md) / EventTooltipContent

# Function: EventTooltipContent()

> **EventTooltipContent**(`breakWindows`): `Element`

Defined in: [ui/src/components/schedule/event-component/EventTooltip.tsx:53](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/event-component/EventTooltip.tsx#L53)

Rich tooltip content displayed on long-hover over any event.
Shows ALL event information regardless of event size.

## Parameters

### breakWindows

The calendar's break windows. An event they split shows
       its real end and a per-piece timeline: its stored `endTime` is only
       start + net working time, which no clock on the grid ever shows.

#### breakWindows?

readonly [`BreakWindow`](../../../../../api-shared/break-windows/type-aliases/BreakWindow.md)[] = `[]`

#### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

#### hoveredEnd?

`number`

#### hoveredStart?

`number`

## Returns

`Element`
