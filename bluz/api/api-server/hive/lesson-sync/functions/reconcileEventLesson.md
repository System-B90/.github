[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-sync](../index.md) / reconcileEventLesson

# Function: reconcileEventLesson()

> **reconcileEventLesson**(`client`, `event`, `action`, `controller?`): `Promise`\<`number` \| `null`\>

Defined in: [ui/src/api-server/hive/lesson-sync.ts:139](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/lesson-sync.ts#L139)

Brings the Hive lesson of a single event in line with the event: creates it
when the event first gets a queue mapping, re-points its rules when the
mapping changes, and deletes it when the mapping (or the event) goes away.

Runs with the editing Segel's own Hive credentials, at event write time —
the queue itself is opened later by the activator (`lesson-activation`).

## Parameters

### client

[`HiveClient`](../../client/classes/HiveClient.md)

A Hive client built from the editing user's session.

### event

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

The event as stored.

### action

`"delete"` \| `"upsert"`

Whether the event still exists or has just been removed.

### controller?

[`DatabaseController`](../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

The iteration's Mongo controller (for course names).

## Returns

`Promise`\<`number` \| `null`\>

The lesson id now backing the event, or null when it has none.
