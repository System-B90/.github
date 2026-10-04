[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-activation](../index.md) / selectLiveEvents

# Function: selectLiveEvents()

> **selectLiveEvents**(`events`, `now`): [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-server/hive/lesson-activation.ts:58](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/hive/lesson-activation.ts#L58)

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
