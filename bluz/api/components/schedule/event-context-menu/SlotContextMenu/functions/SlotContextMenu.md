[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/SlotContextMenu](../index.md) / SlotContextMenu

# Function: SlotContextMenu()

> **SlotContextMenu**(`__namedParameters`): `Element` \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/SlotContextMenu.tsx:33](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/schedule/event-context-menu/SlotContextMenu.tsx#L33)

Right-click menu for empty grid (#859): pastes the clipboard event at the
slot under the pointer, like a desktop paste at the cursor.

## Parameters

### \_\_namedParameters

#### canPaste

`boolean`

False on a past iteration, whose writes the server rejects.

#### onClose

() => `void`

#### onPaste

(`slot`) => `void`

#### target

[`SlotContextMenuTarget`](../type-aliases/SlotContextMenuTarget.md) \| `null`

## Returns

`Element` \| `null`
