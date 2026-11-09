[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/assign](../index.md) / planPersonMove

# Function: planPersonMove()

> **planPersonMove**(`target`, `personId`, `withModifier`, `sourceField?`): [`PersonMovePlan`](../type-aliases/PersonMovePlan.md)

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/assign.ts:58](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/calendar/instructor-dnd/assign.ts#L58)

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
