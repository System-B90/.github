[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-sync](../index.md) / resolveDesiredRules

# Function: resolveDesiredRules()

> **resolveDesiredRules**(`event`, `courseNameById`, `hiveClasses`): `Map`\<`number`, `number`\>

Defined in: [ui/src/api-server/hive/lesson-sync.ts:107](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/hive/lesson-sync.ts#L107)

Resolves an event's shuffle→queue mapping into Hive ids.

A Bluz course *is* a shuffle and a shuffle is 1:1 with a Hive student group,
matched by name — the same rule the curriculum cut uses when it creates
courses for shuffles. A course with no matching Hive group contributes
nothing rather than failing the whole sync.

## Parameters

### event

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

The event carrying `hiveQueues`.

### courseNameById

`Map`\<`string`, `string`\>

Bluz course id → course (shuffle) name.

### hiveClasses

`Class`[]

Hive student groups.

## Returns

`Map`\<`number`, `number`\>

Hive student-group id → Hive queue id.
