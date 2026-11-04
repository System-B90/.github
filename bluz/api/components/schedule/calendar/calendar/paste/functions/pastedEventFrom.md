[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/paste](../index.md) / pastedEventFrom

# Function: pastedEventFrom()

> **pastedEventFrom**(`copied`, `slot`): [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/calendar/calendar/paste.ts:35](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/calendar/calendar/paste.ts#L35)

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
