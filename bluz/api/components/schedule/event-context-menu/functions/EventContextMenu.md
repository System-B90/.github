[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / EventContextMenu

# Function: EventContextMenu()

> **EventContextMenu**(`__namedParameters`): `Element` \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:76](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/schedule/event-context-menu/index.tsx#L76)

Right-click menu for calendar tiles (#706). Every entry acts on *all* the
targeted events, so the single-event and multi-select cases are one code
path — a selection of one is simply the common case.

## Parameters

### \_\_namedParameters

[`EventContextMenuProps`](../type-aliases/EventContextMenuProps.md)

## Returns

`Element` \| `null`
