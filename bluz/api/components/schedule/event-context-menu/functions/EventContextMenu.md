[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / EventContextMenu

# Function: EventContextMenu()

> **EventContextMenu**(`__namedParameters`): `Element` \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:76](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/schedule/event-context-menu/index.tsx#L76)

Right-click menu for calendar tiles (#706). Every entry acts on *all* the
targeted events, so the single-event and multi-select cases are one code
path — a selection of one is simply the common case.

## Parameters

### \_\_namedParameters

[`EventContextMenuProps`](../type-aliases/EventContextMenuProps.md)

## Returns

`Element` \| `null`
