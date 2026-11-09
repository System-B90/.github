[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / duplicateOf

# Function: duplicateOf()

> **duplicateOf**(`event`): [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:59](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/event-context-menu/actions.ts#L59)

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
