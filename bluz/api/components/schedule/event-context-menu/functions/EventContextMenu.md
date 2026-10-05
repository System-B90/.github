[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / EventContextMenu

# Function: EventContextMenu()

> **EventContextMenu**(`__namedParameters`): `Element` \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:104](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/schedule/event-context-menu/index.tsx#L104)

Right-click menu for calendar tiles (#706). Every entry acts on *all* the
targeted events, so the single-event and multi-select cases are one code
path — a selection of one is simply the common case.

## Parameters

### \_\_namedParameters

[`EventContextMenuProps`](../type-aliases/EventContextMenuProps.md)

## Returns

`Element` \| `null`
