[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/use-event-selection](../index.md) / useEventSelection

# Function: useEventSelection()

> **useEventSelection**(`events`): [`EventSelection`](../type-aliases/EventSelection.md)

Defined in: [ui/src/components/schedule/event-context-menu/use-event-selection.ts:30](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/use-event-selection.ts#L30)

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
