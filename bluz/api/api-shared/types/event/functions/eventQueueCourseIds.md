[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / eventQueueCourseIds

# Function: eventQueueCourseIds()

> **eventQueueCourseIds**(`event`): `string`[]

Defined in: [ui/src/api-shared/types/event.ts:120](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/event.ts#L120)

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
