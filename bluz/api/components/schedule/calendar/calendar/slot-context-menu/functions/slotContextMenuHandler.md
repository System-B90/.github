[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/slot-context-menu](../index.md) / slotContextMenuHandler

# Function: slotContextMenuHandler()

> **slotContextMenuHandler**(`open`, `gapAt`): (`pointer`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx:73](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx#L73)

`onContextMenu` for the grid: opens the slot menu on empty grid, leaves the
browser's own menu everywhere else. Tiles stop propagation themselves.

## Parameters

### open

[`OpenSlotContextMenu`](../type-aliases/OpenSlotContextMenu.md) \| `null`

The slot menu opener; null while the calendar is read-only.

### gapAt

[`SlotGapFinder`](../type-aliases/SlotGapFinder.md)

Resolves the empty run around the clicked slot.

## Returns

(`pointer`) => `void`
