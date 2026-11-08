[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/actions](../index.md) / postponedByAWeek

# Function: postponedByAWeek()

> **postponedByAWeek**(`event`): [`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/event-context-menu/actions.ts:42](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/event-context-menu/actions.ts#L42)

The same event a week later. Only the times move — duration, rooms and
every marker are preserved, so a postponed event is the event it was.

## Parameters

### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The event to move.

## Returns

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

The postponed copy.
