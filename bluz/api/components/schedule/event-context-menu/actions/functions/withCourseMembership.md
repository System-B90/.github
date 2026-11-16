[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / withCourseMembership

# Function: withCourseMembership()

> **withCourseMembership**(`event`, `courseId`, `member`): [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:73](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/event-context-menu/actions.ts#L73)

Adds or removes one shuffle (מסלול) from an event, leaving its other
shuffles alone. Order is preserved on removal so the event's course list
doesn't reshuffle itself under the user on every toggle.

## Parameters

### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The event to change.

### courseId

`string`

The shuffle being toggled.

### member

`boolean`

Whether the event should end up in that shuffle.

## Returns

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The updated event.
