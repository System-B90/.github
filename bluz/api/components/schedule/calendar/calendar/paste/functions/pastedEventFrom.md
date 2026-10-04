[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/paste](../index.md) / pastedEventFrom

# Function: pastedEventFrom()

> **pastedEventFrom**(`copied`, `slot`): [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/calendar/calendar/paste.ts:24](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/calendar/calendar/paste.ts#L24)

The new event a paste creates (shared by Ctrl+V and the right-click menus,
#859). It keeps the copied event's duration; with a slot it starts there and
takes the slot's room column, without one it lands 30 minutes after the
original so the copy never hides exactly under it.

## Parameters

### copied

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

The event on the clipboard.

### slot

[`PasteSlot`](../type-aliases/PasteSlot.md) \| `null`

The target slot, or null.

## Returns

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)
