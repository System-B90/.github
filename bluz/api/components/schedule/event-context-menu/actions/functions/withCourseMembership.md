[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / withCourseMembership

# Function: withCourseMembership()

> **withCourseMembership**(`event`, `courseId`, `member`): [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:73](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/event-context-menu/actions.ts#L73)

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
