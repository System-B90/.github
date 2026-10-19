[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-sync](../index.md) / describeUnresolvedShuffles

# Function: describeUnresolvedShuffles()

> **describeUnresolvedShuffles**(`event`, `courseById`, `hiveClasses`): `string`

Defined in: [ui/src/api-server/hive/lesson-sync.ts:136](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/hive/lesson-sync.ts#L136)

Says why each queue-carrying shuffle of an event failed to resolve to a
Hive group: the course is missing from this iteration, or no group matches
its link or name.

## Parameters

### event

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

The event carrying `hiveQueues`.

### courseById

`Map`\<`string`, `Pick`\<[`Course`](../../../../api-shared/types/course/type-aliases/Course.md), `"name"` \| `"hiveClassId"`\>\>

Bluz course id → course (shuffle).

### hiveClasses

`Class`[]

Hive student groups the sync could see.

## Returns

`string`

A one-line log message.
