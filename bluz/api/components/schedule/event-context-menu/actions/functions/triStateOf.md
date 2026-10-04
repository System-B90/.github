[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / triStateOf

# Function: triStateOf()

> **triStateOf**(`events`, `has`): [`TriState`](../type-aliases/TriState.md)

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:25](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/schedule/event-context-menu/actions.ts#L25)

Folds a per-event predicate over the targets.

## Parameters

### events

readonly [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)[]

The events the menu is acting on.

### has

(`event`) => `boolean`

Reads the marker off one event.

## Returns

[`TriState`](../type-aliases/TriState.md)

Whether none, some or all of them carry it.
