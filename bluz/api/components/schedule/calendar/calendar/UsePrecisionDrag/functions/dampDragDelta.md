[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/UsePrecisionDrag](../index.md) / dampDragDelta

# Function: dampDragDelta()

> **dampDragDelta**(`deltaMs`, `isPrecise`): `number`

Defined in: [ui/src/components/schedule/calendar/calendar/UsePrecisionDrag.ts:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar/UsePrecisionDrag.ts#L22)

The delta a drag of `deltaMs` on screen should actually apply. Pure, so the
damping rule is testable without a pointer.

Alt-held drags move (or resize) an event a quarter as far as the pointer
travelled and land on whole minutes (#475). The grid snaps to 5 minutes,
which is coarse for a small correction and forces the user to fight the
snap; holding Alt trades reach for resolution without changing the grid.

The modifier used to be Ctrl, which is claimed by "duplicate the dragged
event" — so a Ctrl+drag duplicate landed at a quarter of the intended offset
(#608). Precision moved to Alt; duplicate keeps Ctrl. Both are read live by
`useDragModifiers`, and the drag preview applies this same rule so what is
drawn mid-drag is exactly what lands on drop.

## Parameters

### deltaMs

`number`

### isPrecise

`boolean`

## Returns

`number`
