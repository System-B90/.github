[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/UseDragModifiers](../index.md) / useResizeKeyGate

# Function: useResizeKeyGate()

> **useResizeKeyGate**(`dragging`): `void`

Defined in: [ui/src/components/schedule/calendar/calendar/UseDragModifiers.ts:118](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/calendar/UseDragModifiers.ts#L118)

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
