[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-activation](../index.md) / selectLiveEvents

# Function: selectLiveEvents()

> **selectLiveEvents**(`events`, `now`): [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-server/hive/lesson-activation.ts:56](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/hive/lesson-activation.ts#L56)

Live, non-hidden events that should open a queue right now.

Hidden events are excluded deliberately: they are not shown to students, so
they must not move students' work either. Sorted by start time so that when
two events overlap for one group, the later one is applied last and wins.

## Parameters

### events

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

Candidate events (already limited to the surrounding window).

### now

`Date`

The moment being evaluated.

## Returns

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

The events to act on, oldest start first.
