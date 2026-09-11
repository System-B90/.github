[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/assign](../index.md) / planPersonMove

# Function: planPersonMove()

> **planPersonMove**(`source`, `target`, `personId`, `withModifier`, `sourceField?`): [`PersonMovePlan`](../type-aliases/PersonMovePlan.md)

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/assign.ts:57](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/instructor-dnd/assign.ts#L57)

Decides whether a person can move between two events, and into which field.

## Parameters

### source

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md) \| `undefined`

The event the chip was dragged out of.

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
