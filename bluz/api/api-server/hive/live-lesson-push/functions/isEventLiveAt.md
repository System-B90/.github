[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/live-lesson-push](../index.md) / isEventLiveAt

# Function: isEventLiveAt()

> **isEventLiveAt**(`event`, `now`): `boolean`

Defined in: [ui/src/api-server/hive/live-lesson-push.ts:55](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-server/hive/live-lesson-push.ts#L55)

Whether an event is running right now and carries a Hive lesson for some
course: the same gate the activator uses, without its lateness cap — an
edit made at any point of a running event should reach Hive.

## Parameters

### event

`Pick`\<[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md), `"archived"` \| `"courses"` \| `"endTime"` \| `"hidden"` \| `"hiveLesson"` \| `"parked"` \| `"startTime"`\>

The event to inspect.

### now

`Date`

The moment being evaluated.

## Returns

`boolean`

Whether the event currently holds its groups' lesson.
