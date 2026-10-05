[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-sync](../index.md) / resolveDesiredRules

# Function: resolveDesiredRules()

> **resolveDesiredRules**(`event`, `courseById`, `hiveClasses`): `Map`\<`number`, `number`\>

Defined in: [ui/src/api-server/hive/lesson-sync.ts:107](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/hive/lesson-sync.ts#L107)

Resolves an event's shuffle→queue mapping into Hive ids.

A Bluz course *is* a shuffle and a shuffle is 1:1 with a Hive student group,
its explicitly linked group, else the same-named one (#774). A course with no matching Hive group contributes
nothing rather than failing the whole sync.

## Parameters

### event

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

The event carrying `hiveQueues`.

### courseById

`Map`\<`string`, `Pick`\<[`Course`](../../../../api-shared/types/course/type-aliases/Course.md), `"name"` \| `"hiveClassId"`\>\>

Bluz course id → course (shuffle).

### hiveClasses

`Class`[]

Hive student groups.

## Returns

`Map`\<`number`, `number`\>

Hive student-group id → Hive queue id.
