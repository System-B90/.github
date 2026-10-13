[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/UseDragModifiers](../index.md) / useResizeKeyHeld

# Function: useResizeKeyHeld()

> **useResizeKeyHeld**(`dragging`): `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar/UseDragModifiers.ts:111](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/schedule/calendar/calendar/UseDragModifiers.ts#L111)

Whether resizing is unlocked (#961). Dragging a tile always moves it; its
edges only resize while Shift is held, so a move never resizes by accident.
Frozen during a drag, so letting go of Shift mid-resize doesn't pull the
resize handles out from under the pointer.

## Parameters

### dragging

() => `boolean`

## Returns

`boolean`
