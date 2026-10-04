[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/use-event-selection](../index.md) / useEventSelection

# Function: useEventSelection()

> **useEventSelection**(`events`): [`EventSelection`](../type-aliases/EventSelection.md)

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:30](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L30)

Multi-selection of calendar tiles (#706). Held above the calendar because
both the grid (which draws the selection ring) and the right-click menu
(which acts on it in bulk) read it.

## Parameters

### events

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)[]

The events currently loaded into the calendar.

## Returns

[`EventSelection`](../type-aliases/EventSelection.md)

The selection and the operations that mutate it.
