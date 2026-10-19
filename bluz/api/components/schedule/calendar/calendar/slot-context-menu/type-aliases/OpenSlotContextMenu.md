[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/slot-context-menu](../index.md) / OpenSlotContextMenu

# Type Alias: OpenSlotContextMenu

> **OpenSlotContextMenu** = (`slot`, `clientX`, `clientY`, `gap`) => `void`

Defined in: [ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx:13](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx#L13)

Right-click on an empty grid slot, in viewport coordinates (#859). `gap` is
the empty run around the slot in its column, null when the slot is covered.

## Parameters

### slot

[`PasteSlot`](../../paste/type-aliases/PasteSlot.md)

### clientX

`number`

### clientY

`number`

### gap

[`Interval`](../../../../../../api-shared/interval-layout/type-aliases/Interval.md) \| `null`

## Returns

`void`
