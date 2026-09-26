[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / withCourseMembership

# Function: withCourseMembership()

> **withCourseMembership**(`event`, `courseId`, `member`): [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:70](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-context-menu/actions.ts#L70)

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
