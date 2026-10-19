[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/SlotContextMenu](../index.md) / SlotContextMenu

# Function: SlotContextMenu()

> **SlotContextMenu**(`__namedParameters`): `Element` \| `null`

Defined in: [ui/src/components/schedule/event-context-menu/SlotContextMenu.tsx:41](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/SlotContextMenu.tsx#L41)

Right-click menu for empty grid (#859): pastes the clipboard event at the
slot under the pointer, like a desktop paste at the cursor, drops a break
there, or fills the empty run around it with a general ע"ע.

## Parameters

### \_\_namedParameters

#### canFill

`boolean`

False while the "כללי" Hive subject is unknown.

#### canPaste

`boolean`

#### onAddBreak

(`slot`) => `void`

#### onClose

() => `void`

#### onFillGap

(`slot`, `gap`) => `void`

#### onPaste

(`slot`) => `void`

#### readOnly

`boolean`

A past iteration, whose writes the server rejects.

#### target

[`SlotContextMenuTarget`](../type-aliases/SlotContextMenuTarget.md) \| `null`

## Returns

`Element` \| `null`
