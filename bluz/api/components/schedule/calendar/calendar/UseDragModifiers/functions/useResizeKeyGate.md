[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/UseDragModifiers](../index.md) / useResizeKeyGate

# Function: useResizeKeyGate()

> **useResizeKeyGate**(`dragging`): `void`

Defined in: [ui/src/components/schedule/calendar/calendar/UseDragModifiers.ts:129](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/calendar/calendar/UseDragModifiers.ts#L129)

Gates resizing behind Shift (#961). Dragging a tile always moves it; its
edges only resize while Shift is held, so a move never resizes by accident.
Frozen during a drag, so letting go of Shift mid-resize doesn't pull the
resize handles out from under the pointer.

The gate is an attribute on `<html>` that CSS reads to show the handles,
not React state: flipping `resizableAccessor` re-rendered every tile in
view on each Shift press (#987).

## Parameters

### dragging

() => `boolean`

## Returns

`void`
