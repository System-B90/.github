[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/utils](../index.md) / buildGanttEventLink

# Function: buildGanttEventLink()

> **buildGanttEventLink**(`event`, `iterationId?`): `string` \| `undefined`

Defined in: [ui/src/components/schedule/event-dialog/utils.ts:18](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/event-dialog/utils.ts#L18)

Builds the "go to gantt event" link. `gc` and `it` must both ride along
or the gantt page has no curriculum/iteration to load and `ge` is a
no-op (#…). Returns undefined when the event has no gantt curriculum
linkage — old cut events, or events never cut — so the caller can hide
the link entirely instead of shipping a dead one.

## Parameters

### event

`Pick`\<`Partial`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)\>, `"ganttCurriculumId"` \| `"ganttEventId"`\>

### iterationId?

`string` \| `null`

## Returns

`string` \| `undefined`
