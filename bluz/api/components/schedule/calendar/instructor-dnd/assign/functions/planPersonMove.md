[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/assign](../index.md) / planPersonMove

# Function: planPersonMove()

> **planPersonMove**(`target`, `personId`, `withModifier`, `sourceField?`): [`PersonMovePlan`](../type-aliases/PersonMovePlan.md)

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/assign.ts:57](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/schedule/calendar/instructor-dnd/assign.ts#L57)

Decides whether a person can move onto an event, and into which field.

## Parameters

### target

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

The event it was dropped on.

### personId

[`PersonId`](../../../../../../api-shared/types/event/type-aliases/PersonId.md)

The person being moved.

### withModifier

`boolean`

Whether Shift was held at drop time.

### sourceField?

[`PersonField`](../../types/type-aliases/PersonField.md)

The field the chip sat in on the source event.

## Returns

[`PersonMovePlan`](../type-aliases/PersonMovePlan.md)
