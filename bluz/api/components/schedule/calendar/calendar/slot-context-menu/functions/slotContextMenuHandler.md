[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/slot-context-menu](../index.md) / slotContextMenuHandler

# Function: slotContextMenuHandler()

> **slotContextMenuHandler**(`open`): (`pointer`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx:57](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx#L57)

`onContextMenu` for the grid: opens the slot menu on empty grid, leaves the
browser's own menu everywhere else. Tiles stop propagation themselves.

## Parameters

### open

[`OpenSlotContextMenu`](../type-aliases/OpenSlotContextMenu.md) \| `null`

The slot menu opener; null while the calendar is read-only.

## Returns

(`pointer`) => `void`
