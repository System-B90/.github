[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/slot-context-menu](../index.md) / slotUnderPointer

# Function: slotUnderPointer()

> **slotUnderPointer**(`clientX`, `clientY`, `root?`): [`PasteSlot`](../../paste/type-aliases/PasteSlot.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx:54](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx#L54)

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
