[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / duplicateOf

# Function: duplicateOf()

> **duplicateOf**(`event`): [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:57](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/schedule/event-context-menu/actions.ts#L57)

A brand-new event seeded from an existing one, in the same slot. The grid
lays the two side by side, which is what makes the copy visible without
guessing at a free slot to drop it into — the user then drags it where it
belongs (or undoes).

## Parameters

### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The event to copy.

## Returns

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The new event, ready to save (the provider assigns its id).
