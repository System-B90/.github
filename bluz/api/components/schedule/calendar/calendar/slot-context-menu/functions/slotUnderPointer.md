[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/slot-context-menu](../index.md) / slotUnderPointer

# Function: slotUnderPointer()

> **slotUnderPointer**(`clientX`, `clientY`, `root?`): [`PasteSlot`](../../paste/type-aliases/PasteSlot.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx:42](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx#L42)

The grid slot under the pointer, or null outside a day column (the time
gutter, headers, all-day row).

## Parameters

### clientX

`number`

Pointer x in viewport coordinates.

### clientY

`number`

Pointer y in viewport coordinates.

### root?

`Document` = `document`

Document to search; injectable for tests.

## Returns

[`PasteSlot`](../../paste/type-aliases/PasteSlot.md) \| `null`
