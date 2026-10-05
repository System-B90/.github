[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventQueueCourseIds

# Function: eventQueueCourseIds()

> **eventQueueCourseIds**(`event`): `string`[]

Defined in: [ui/src/api-shared/types/event.ts:120](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/types/event.ts#L120)

The shuffles (Bluz course ids) of an event that carry a Hive queue, i.e. the
groups whose students should get a queue opened when the event goes live.
Only courses the event is actually assigned to count — a stale mapping left
behind by removing a course must not open a queue for it.

## Parameters

### event

`Pick`\<[`Event`](../type-aliases/Event.md), `"courses"` \| `"hiveQueues"`\>

The event to inspect.

## Returns

`string`[]

The mapped course ids, in the event's own course order.
