[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/schedule/event-context-menu](../index.md) / EventContextMenu

# Function: EventContextMenu()

> **EventContextMenu**(`__namedParameters`): `Element` \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/index.tsx:96](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/schedule/event-context-menu/index.tsx#L96)

Right-click menu for calendar tiles (#706). Every entry acts on *all* the
targeted events, so the single-event and multi-select cases are one code
path — a selection of one is simply the common case.

## Parameters

### \_\_namedParameters

[`EventContextMenuProps`](../type-aliases/EventContextMenuProps.md)

## Returns

`Element` \| `null`
